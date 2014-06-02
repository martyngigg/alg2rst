'''
Created on 28 Apr 2014

@author: James McCarthy

Small script to update the image links to look for the image files in an images folder

'''

import os

pagesWithImages = []

#Uses the old links as the search term and replaces them with the new links    
def updateImageDir(algName, algDir):
    print "ALGNAME", algName
    with open (algDir+algName+'.rst', 'r') as algFile:
        rst=algFile.read()        
        before = rst
      
    rst = rst.replace('.. figure:: ', '.. figure:: images\\')
    #rst = rst.replace('.. figure:: images\\', '.. figure:: ')
    
    #See if any update was made to page
    if before != rst:        
        pagesWithImages.append(algName)
     
    fixedFile = open(algDir+algName+'.rst', 'w')
    fixedFile.write(rst)

def updateImages(convertedDir):
    
    algNames = []
    
    #For each algorithm file run the converter    
    for subdir, dirs, files in os.walk(convertedDir):
        for alg in files:
            algName = os.path.splitext(alg)[0]
            updateImageDir(algName, convertedDir)
            
    print 'Image links updated, this is a list of pages with images:'
    print pagesWithImages
    print '\nExtra Info:'
    print 'Update UnwrapSNS & AbsorptionCorrection image link by hand - as it is defined as a file for an image it doesnt work currently'
    print 'Alter the image names in RingProfile as two images are called RingProfileInstrument.png'
    
if __name__ == '__main__':   
    updateImages('C:/Users/mrn39220/Documents/workspace/ALGexport/ConvertedRST/')