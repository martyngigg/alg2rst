'''
Created on 1 May 2014

This script uses the template file to insert the directives for each algorithm rst file so that it can later be merged with the relevant info.

@author: James McCarthy
'''

import os, sys

from mantid import AlgorithmFactory, FunctionFactory

FUNC_NAMES = FunctionFactory.getFunctionNames()


def create(algName, convertedDir):
    #read the rst content in
    with open (convertedDir+algName+'.rst', 'r') as rstFile:
        rst=rstFile.read()
    
    #remove extra whitespace and newlines from the end of the documentation
    rst = rst.rstrip()
    template_dir = os.path.dirname(__file__)

    if AlgorithmFactory.exists(algName):
        template_file = os.path.join(template_dir,'algorithm_template.rst')
    elif AlgorithmFactory.exists(algName[:-3]):
        template_file = os.path.join(template_dir,'algorithm_template.rst')
    elif algName in FUNC_NAMES:
        template_file = os.path.join(template_dir,'function_template.rst')
    elif "USAGE" in algName:
        raise RuntimeError("Usage section rst encountered in directive insertion: %s" % algName)
    else:
        raise RuntimeError("Unknown object in directive insertion: %s" % algName)

    with open (template_file, 'r') as templateFile:
        template=templateFile.read()

    built = template.replace('[TITLE]', "="*len(algName) + "\n" + algName + "\n" + "="*len(algName) + "\n")
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