'''
Created on 28 Apr 2014

@author: James McCarthy

Small script to update the image links to look for the image files in an images folder

'''

import os
import re

pagesWithImages = []


IMAGE_NAME_RE = re.compile(r".. figure:: images/(.+)")

#Uses the old links as the search term and replaces them with the new links    
def updateImageDir(algName, algDir):
    with open (algDir+algName+'.rst', 'r') as algFile:
        rst=algFile.read()        
        before = rst
      
    rst = rst.replace('.. figure:: ', '.. figure:: images/')
    
    #See if any update was made to page
    if before != rst:
        match = IMAGE_NAME_RE.search(rst)
        if match is not None:
            filename = match.group(1)
        else:
            raise RuntimeError("No match %s" % rst)
        pagesWithImages.append((algName,filename))
     
    fixedFile = open(algDir+algName+'.rst', 'w')
    fixedFile.write(rst)

def updateImages(convertedDir):
    
    algNames = []
    
    #For each algorithm file run the converter    
    for subdir, dirs, files in os.walk(convertedDir):
        for alg in files:
            algName = os.path.splitext(alg)[0]
            updateImageDir(algName, convertedDir)
    ###

    with open("images.txt", "w") as images_files:
        txt = 'Image links updated, this is a list of pages with images:\n'
        for name, filename in pagesWithImages:
            txt += "    " + name + ": " + filename + "\n"
        ###
        txt += \
            '\nExtra Info\n:' + \
            'Update UnwrapSNS & AbsorptionCorrection image link by hand - as it is defined as a file for an image it doesnt work currently\n' + \
            'Alter the image names in RingProfile as two images are called RingProfileInstrument.png\n'
        images_files.write(txt + "\n")
    ####
    
if __name__ == '__main__':   
    updateImages('C:/Users/mrn39220/Documents/workspace/ALGexport/ConvertedRST/')
