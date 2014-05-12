'''
Created on 23 Apr 2014

This converter works by parsing the individual algorithms documentation rst files and finding links and storing the links in a list. 
It then compares these links against known algorithm link names and generates a reference type link for any links that are linking to
algorithms. It then replaces all existing algorithm links in the document with the new format reference link

@author: James McCarthy
'''

import sys, subprocess, os, shutil, re, fileinput
from collections import defaultdict
links_todo = defaultdict(list)

concepts = ['Algorithm','Geometry','Instrument','Lattice','Logging','Plugin','Project','Properties','Run','SpectraDetectorMap','Workspace']

#Finds links within a document and returns them
def findLinks(algName, algDir):
    
    #Open each given file and read the contents as a string
    with open (algDir+algName+'.rst', 'r') as algFile:
        algRSTstr=algFile.read()
    
    p = re.compile(r'`\w+\s\<\w+\>`__')
    matches = p.findall(algRSTstr)
    
    if len(matches) <=0:
        return None
    else:    
        return matches

#Replace links of this format: `link <link>`__ with: :ref:`link` 
def genNewLinks(links, algNames, pageName):
    
    repLinks = []
    
    for link in links:
        link = link.replace('`', '')
        link = link.replace('<', '')
        link = link.replace('>', '')
        link = link.replace('__', '')
        link = link.split()

        #Check length of link
        if len(link) > 2:
            print 'Unlikely to be an algorithm link with multiple words in it'
            print link
            repLinks.append(None)
            links_todo[pageName].append(link)      
        else:            
            name = link[0]            
            #Check if the link is a concept
            if name in concepts or 'workspace' in name or 'Workspace' in name or name in algNames:
                newLink = ':ref:`'+name+'`'
                repLinks.append(newLink)
            else:
                #These are links that aren't algorithms but are single words links, likely to be links to concepts or similar
                #print 'Not found in algorithm list'
                repLinks.append(None)
                links_todo[pageName].append(link)
    
    return repLinks

#Uses the old links as the search term and replaces them with the new links    
def replaceLinks(oldLinks, newLinks, algName, algDir):
    
    with open (algDir+algName+'.rst', 'r') as algFile:
        rst=algFile.read()        
            
    for old, new in zip(oldLinks, newLinks):
        if new != None:
            print 'Replacing:',old
            print 'With:',new        
            rst = rst.replace(old, new)
        
    fixedFile = open(algDir+algName+'.rst', 'w')
    fixedFile.write(rst)

def convert(convertedDir):  

    algNames = []
    
    #Create a list of all algorithm names to use as a lookup
    for subdir, dirs, files in os.walk(convertedDir):
        for alg in files:
            algName = os.path.splitext(alg)[0]
            algNames.append(algName)
    
    algNames = list(set(algNames))
    
    #For each algorithm file run the converter
    for subdir, dirs, files in os.walk(convertedDir):
        for alg in files:
            algName = os.path.splitext(alg)[0]
    
            links = findLinks(algName, convertedDir)
            
            if links != None:     
                repLinks = genNewLinks(links, algNames, algName)
                #print repLinks
                #replaceLinks(links, repLinks, algName, convertedDir)
            else:
                #print 'No links found in', algName
                repLinks = None  
    
    ##Print out a list of links that still need manually fixing
    #print '\n=============================\nPages with links that need updating:\n'
    count=0    
    for key, links in links_todo.items():
        print key #This is the page name that the link is one
        for link in links:
            print link  #The links that need fixing manually
            count+=1
        print '========='
    print count #The number of links that need hand fixing
        
def convertLinks(conDir, conUsageDir):
    convert(conDir)
    convert(conUsageDir) 

if __name__ == '__main__':   
    convertLinks('C:/Users/mrn39220/Documents/workspace/ALGexport/ConvertedRST/',
                 'C:/Users/mrn39220/Documents/workspace/ALGexport/ConvertedUsageRST/')        