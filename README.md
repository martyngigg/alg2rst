#alg2rst


Mantid MediaWiki Algorithms to RST 

This converter is designed for a single use to extract the documentation from Mantid algorithms and convert them to RST. It can also remove the documentation from the Mantid CCP files. 

##How to Use:

alg2rst is made up of 4 classes. 
  _convertMWtoRST  - This class will fetch the documentation from the CPP files and convert to RST. The convertMWtoRST function is supplied with a boolean which when true will remove the wiki and usage markup from the CPP files. (Cleanup) 
  
  _convertLinks - This class uses a list of all the algorithm names which it fetches from the file names and also a list of concepts and will udpate any algorithms, concepts or workspace links to be reference links that will work internally with sphyinx. 
  
  _updateImages - Makes a small change to the image links to point the image to the images folder
  
  _insertDirectives - This uses the template.rst to update each algorithm rst file into the format required for use with our own sphyinx module. This class  replaces the [ALGNAME] tag in the template with the correct algoritm name and the [DOCUMENTATION] tag with the rst generated for the algorthm and saves the output. 
  

Each of these classes can be run seperately or the class runConverters can be used to run the entire suite. runConverters requires a few paths to be specified so the converter will work: 
```python
algDir = '' #Path to the mantid framework folder
conDir =  '' #Folder where the converted RST files of the algorithms will be saved
conUsageDir = '' #Folder where the converted usage documentents will be saved
tempDir = '' #A temp folder which can be used during the conversion
```
