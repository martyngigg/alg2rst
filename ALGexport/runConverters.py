'''
Created on 28 Apr 2014

This script allows running of the whole suite of scripts to extract documentation and export it as RST files

@author: James McCarthy
'''

import convertMWtoRST, convertLinks, updateImages, insertDirectives, sortToDirectory

algDir = '/home/dmn58364/GitHub/mantid/Code/Mantid/Framework/' #Path to the mantid framework folder
conDir = '/home/dmn58364/GitHub/mantid/Code/Mantid/docs/source/' #Folder where the converted RST files of the algorithms will be saved
conUsageDir = '/mnt/data1/SaveDir/ConvertedUsageRST/' #Folder where the converted usage documentents will be saved
tempDir = '/mnt/data1/SaveDir/tmp/'  #A temp folder which can be used during the conversion
sortedOutput = algDir

if __name__ == '__main__':

    convertMWtoRST.init(algDir, conDir, conUsageDir, tempDir) #Set the paths and empty folder were RST will be stored
    convertMWtoRST.convertMWtoRST(clean=True)
    convertLinks.convertLinks(conDir, conUsageDir)
    updateImages.updateImages(conDir + "algorithms/")
    updateImages.updateImages(conDir + "functions/")
    insertDirectives.insertDirectives(conDir + "algorithms/")
    insertDirectives.insertDirectives(conDir + "functions/")
    #sortToDirectory.sortToDirectory(algDir, sortedOutput, conDir)
