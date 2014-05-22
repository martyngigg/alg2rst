'''
Created on 1 May 2014

This script uses the template file to insert the directives for each algorithm rst file so that it can later be merged with the relevant info.

@author: James McCarthy
'''

import os, sys

def create(algName, convertedDir):
    #read the rst content in
    with open (convertedDir+algName+'.rst', 'r') as rstFile:
        rst=rstFile.read()
    
    #remove extra whitespace and newlines from the end of the documentation
    rst = rst.rstrip()
    template_dir = os.path.dirname(__file__)
    #os.chdir(pathname) 
    with open (os.path.join(template_dir,'template.rst'), 'r') as templateFile:
        template=templateFile.read()
    
    built = template.replace('[ALGNAME]', algName)
    built = built.replace('[DOCUMENTATION]', rst)
    
    builtFile = open(convertedDir+algName+'.rst', 'w')
    builtFile.write(built)
    
    
def insertDirectives(convertedDir):
 
    #For each algorithm file run the converter    
    for subdir, dirs, files in os.walk(convertedDir):
        for alg in files:
            algName = os.path.splitext(alg)[0]             
            create(algName, convertedDir)
            print 'Building:'+algName
    
    print 'Merge Complete'
    
if __name__ == '__main__':   
    insertDirectives('C:/Users/mrn39220/Documents/workspace/ALGexport/ConvertedRST/')