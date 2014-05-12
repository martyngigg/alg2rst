'''
Created on 28 Apr 2014

This script allows running of the whole suite of scripts to extract documentation and export it as RST files

@author: James McCarthy
'''

import convertMWtoRST, convertLinks, updateImages, insertDirectives

algDir = 'C:/Mantid/Code/Mantid/Framework/' #Path to the mantid framework folder
conDir = 'C:/Users/mrn39220/Documents/workspace/ALGexport/ConvertedRST/' #Folder where the converted RST files of the algorithms will be saved
conUsageDir = 'C:/Users/mrn39220/Documents/workspace/ALGexport/ConvertedUsageRST/' #Folder where the converted usage documentents will be saved
tempDir = 'C:/Users/mrn39220/Documents/workspace/ALGexport/Temp/'  #A temp folder which can be used during the conversion

if __name__ == '__main__':
    convertMWtoRST.init(algDir, conDir, conUsageDir, tempDir) #Set the paths and empty folder were RST will be stored
    convertMWtoRST.convertMWtoRST(False)
    convertLinks.convertLinks(conDir, conUsageDir)
    updateImages.updateImages(conDir)
    insertDirectives.insertDirectives(conDir)