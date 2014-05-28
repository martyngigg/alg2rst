'''
Created on 19 May 2014

@author: mrn39220
'''

import sys, subprocess, os, shutil
from os.path import basename

def mapDirectory(algDir):  
    
    dirMap = {}
        
    for dirpath, dnames, fnames in os.walk(algDir):
        for f in fnames:
            if f.endswith('.cpp') or f.endswith('.py'):
                path = (os.path.join(dirpath, f))                
                filename = basename(path)
                algName = os.path.splitext(filename)[0]
                ext =  os.path.splitext(filename)[1]                                                
                path = path.replace(algDir,'')
                path = path.replace(algName+ext,'')                                

                path = path.split("/")[0] # only works on Linux!!
                path += "/doc/"
                dirMap[algName] = path
    
    return dirMap

def copyAlgToTree(dirMap, rstDir, outputDir):
    
    for dirpath, dnames, fnames in os.walk(rstDir):
        for f in fnames:
            if f.endswith('.rst'):                
                path = (os.path.join(dirpath, f))      
                filename = basename(path)
                algName = os.path.splitext(filename)[0]
                ext =  os.path.splitext(filename)[1]
                directory = outputDir+dirMap[algName]
                
                if not os.path.exists(directory):                    
                    os.makedirs(directory)
                shutil.move(path, directory)
      
    
#Create the output folder also empty it if it exists already
def initOutputDir(outputDir):
    if os.path.exists(outputDir):
        shutil.rmtree(outputDir)
    os.makedirs(outputDir)

    
def sortToDirectory(algDir, outputDir, rstDir):
    #initOutputDir(outputDir + "")
    dirMap = mapDirectory(algDir)
    copyAlgToTree(dirMap, rstDir, outputDir)
    print 'Sorting completed. Find the finished output in the folder: ' +outputDir
if __name__ == '__main__':
    sortToDirectory('C:/Mantid/Code/Mantid/Framework/', 'C:/Users/mrn39220/Documents/workspace/ALGexport/Framework/', 'C:/Users/mrn39220/Documents/workspace/ALGexport/ConvertedRST/')
    
    
    