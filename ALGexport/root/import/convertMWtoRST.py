'''
Created on 22 Apr 2014

This script opens each .cpp file in the specified directory recursively and looks for wiki and wiki_usage tags. If they exist
this content is extracted and stored in a temporary text file. It is then convert to RST format with Pandoc which is commanded
via the command line. The script then stores the converted RST files in two folders, one for the main wiki documentation and one
for the usage documentation. This script also accepts and optional argument to delete the wiki and wiki_usage section from the 
cpp files once it has been extracted.

@author: James McCarthy
'''
#TODO: Read all src files from the frameworks folder and look for the tags DONE 
#TODO: Delete wiki and wiki usage tags option when running the script DONE
#TODO: Create separate RST file for USAGE section instead of folding it in with the WIKI section, DONE
#TODO: Add tags for each section that will be auto added, usage, breadcrumbs, table, GUI screenshot DONE
#TODO: Support py files DONE
#TODO: Add concept refs
import sys, subprocess, os, shutil
from os.path import basename

#Return content found inside the given strings
def findByTag(algorithmStr, algName, ext):
    

    if ext == '.cpp':
        wikiOpen = '/*WIKI*'
        wikiClose= '*WIKI*/'
        wOffset = 7
        wikiUOpen = '/*WIKI_USAGE*'
        wikiUClose= '*WIKI_USAGE*/'
        wuOffset = 14
        wikiUNSOpen = '/*WIKI_USAGE_NO_SIGNATURE*'
        wikiUNSClose= '*WIKI_USAGE_NO_SIGNATURE*/'
        wunsOffset = 27
    else:
        wikiOpen = '"""*WIKI*'
        wikiClose= '*WIKI*"""'
        wOffset = 9
        wikiUOpen = '"""*WIKI_USAGE*'
        wikiUClose= '*WIKI_USAGE*"""'
        wuOffset = 16
        wikiUNSOpen = '"""*WIKI_USAGE_NO_SIGNATURE*'
        wikiUNSClose= '*WIKI_USAGE_NO_SIGNATURE*"""'
        wuOffset = 30
    
    
    markup = []
    endOfFile = len(algorithmStr)
    endW = 0
    endU = 0
    endUNS = 0
    #For each tag grab the content between these tags, if the tags don't exist return None       
    start = algorithmStr.find(wikiOpen)
        
    if start == -1:
        print 'No wiki information for: '+algName
        markup.append(None)
        endW=0
    else:
        start += wOffset                
        endW = algorithmStr.find(wikiClose)                
        #If no closing tag is found then stop execution so the user can fix this    
        if endW == -1:
            print 'WIKI closing tag not found for: '+algName+'. Halting conversion.'
            sys.exit(1);            
        markup.append(algorithmStr[start:endW].strip())        
    
    #Find usage section if it exists
    start = algorithmStr.find(wikiUOpen)
        
    if start != -1:
        start += wuOffset
        endU = algorithmStr.find(wikiUClose)
        #If no closing tag is found then stop execution so the user can fix this    
        if endU == -1:            
            print 'WIKI_USAGE closing tag not found for: '+algName+'. Halting conversion.'
            sys.exit(1);
        markup.append(algorithmStr[start:endU].strip()) 
    else:                   
        markup.append(None)
        endU=0           
    
    uNoSig = False
    #No usage section was found lets look for a no signature usage section
    if start == -1:
        start = algorithmStr.find(wikiUNSOpen)
        #If a usage no signature was found delete the previous empty element from markup and add this usage
        if start != -1:
            start += wunsOffset
            endUNS = algorithmStr.find(wikiUNSClose)
            if endUNS == -1:            
                print 'WIKI_USAGE_NO_SIGNATURE closing tag not found for: '+algName+'. Halting conversion.'
                sys.exit(1);
            markup.pop() #remove the empty element from the list
            markup.append(algorithmStr[start:endUNS].strip())
            uNoSig = True


    #Store the cpp content without documentation
    if markup[1] == None:
        markup.append(algorithmStr[endW+wOffset:endOfFile].strip())
    else:
        if uNoSig == False:
            markup.append(algorithmStr[endU+wuOffset:endOfFile].strip())
        else:
            markup.append(algorithmStr[endUNS+wunsOffset:endOfFile].strip())
    
    #return a list that contains the wiki and usage if defined
    return markup
        

#Uses pandoc to convert from mediawiki to rst
def convert(algName, algDir, remove, ext):
   
    print 'Converting: '+algName

    with open (algDir+algName+ext, 'r') as algFile:
        algorithmStr=algFile.read()
    
    #Extract the documentation from the string
    markup = findByTag(algorithmStr, algName, ext)
    
    '''
    If remove has been specified then remove the WIKI or WIKI_USAGE section from the cpp
    by replacing the section with an empty string
    '''
    if remove:
        cleanFile = open(algDir+algName+ext, 'w')
        cleanFile.write(markup[2])
    
            
    #If no documentation was present return 0
    if markup[0] == None:
        return 0
    
    wiki = markup[0]
    
    #Store the mediawiki content in a text file
    mwContent = open(tempDir+algName+'.txt', 'w')
    mwContent.write(wiki)
    mwContent.close()
    
    #If there was a usage section store this in a separate file for conversion
    if markup[1] != None:
        usage = markup[1] 
        #Create new text file for usage
        mwContent = open(tempDir+algName+'_USAGE.txt', 'w')
        mwContent.write(usage)
        mwContent.close()
    else:
        usage = None
            
    #Convert main body of documentation to RST        
    convertToRST(algName, tempDir, convertedDir)
    
    if usage != None:
        #If a usage section was present then convert the usage sections to RST and store in another folder
        convertToRST(algName+'_USAGE', tempDir, convertedUsageDir)

def convertToRST(algName, tempDir, convertedDir):
    #Set input name and change working directory
    inputN = algName+'.txt'
    outputN = algName+'.rst'        
        
    os.chdir(tempDir)
    args = ['pandoc', '-f', 'mediawiki', '-t', 'rst', inputN, '-o', outputN]
    
    #run pandoc and wait for output
    obj = subprocess.Popen(args)    
    obj.wait()  
        
    #move completed rst file into completed folder for tidyness
    mvFile = tempDir+algName+'.rst'    
    shutil.move(mvFile, convertedDir)
        
def emptyFolder(folder): 
    
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print e
            
def convertMWtoRST(clean):

    
    #Begin by emtpying the ConvertedRST folder of previous conversions

    print 'Converted folders cleaned. Beginning conversion.'
    
    for dirpath, dnames, fnames in os.walk(algDir):
        for f in fnames:
            if f.endswith('.cpp') or f.endswith('.py'):
                path = (os.path.join(dirpath, f))                
                filename = basename(path)
                algName = os.path.splitext(filename)[0]
                ext =  os.path.splitext(filename)[1]                
                convert(algName, dirpath+os.sep, clean, ext)
                

def init(algDirectory, conDir, conUsageDir, tempPath):
    global algDir    
    algDir = algDirectory
    global convertedDir
    convertedDir = conDir
    global convertedUsageDir
    convertedUsageDir = conUsageDir
    global tempDir
    tempDir = tempPath

    emptyFolder(convertedDir)
    emptyFolder(convertedUsageDir)

    
if __name__ == '__main__':
    init('C:/Mantid/Code/Mantid/Framework/',
         'C:/Users/mrn39220/Documents/workspace/ALGexport/ConvertedRST/',
         'C:/Users/mrn39220/Documents/workspace/ALGexport/ConvertedUsageRST/',
         'C:/Users/mrn39220/Documents/workspace/ALGexport/Temp/')    
    convertMWtoRST(False)
    
    
    
        
        


    
