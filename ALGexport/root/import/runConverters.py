'''
Created on 28 Apr 2014

This script allows running of the whole suite of scripts to extract documentation and export it as RST files

@author: James McCarthy
'''

import convertMWtoRST, convertLinks, updateImages, insertDirectives, sortToDirectory

algDir = '/home/dmn58364/GitHub/mantid/Code/Mantid/Framework/' #Path to the mantid framework folder
conDir = '/home/dmn58364/GitHub/mantid/Code/Mantid/docs/source/algorithms/' #Folder where the converted RST files of the algorithms will be saved
conUsageDir = '/mnt/data1/SaveDir/RST/ConvertedUsageRST/' #Folder where the converted usage documentents will be saved
tempDir = '/mnt/data1/SaveDir/RST/tmp/'  #A temp folder which can be used during the conversion
sortedOutput = algDir

if __name__ == '__main__':
    convertMWtoRST.init(algDir, conDir, conUsageDir, tempDir) #Set the paths and empty folder were RST will be stored
    convertMWtoRST.convertMWtoRST(False)
    convertLinks.convertLinks(conDir, conUsageDir)
    updateImages.updateImages(conDir)
    insertDirectives.insertDirectives(conDir)
    #sortToDirectory.sortToDirectory(algDir, sortedOutput, conDir)
