#alg2rst


Mantid MediaWiki Algorithms to RST 

This converter is designed for a single use to extract the documentation from Mantid algorithms and convert them to RST. It can also remove the documentation from the Mantid CPP and PY files. The output of alg2rst will be two folders, one containing RST files with directives and the documentation section completed with restructeredText for all algorithms that defined a WIKI tag in its CPP/PY file. A second folder with which contains restructeredText of the usage section of any algoirthms that defined a WIKI_USAGE tag in its CPP/PY file. 

##Requirments
alg2rst requires Pandoc to be installed and available on the command line. Install instructions for Pandoc can be found here: http://johnmacfarlane.net/pandoc/installing.html

##How to Use:

alg2rst is made up of 4 classes. 

  *convertMWtoRST* - This class will fetch the documentation from the CPP files and convert to RST. The convertMWtoRST function is supplied with a boolean which when true will remove the wiki and usage markup from the CPP files. (Cleanup) 
  
  *convertLinks* - This class uses a list of all the algorithm names which it fetches from the file names and also a list of concepts and will udpate any algorithms, concepts or workspace links to be reference links that will work internally with sphyinx. 
  
  *updateImages* - Makes a small change to the image links to point the image to the images folder
  
  *insertDirectives* - This uses the template.rst to update each algorithm rst file into the format required for use with our own sphyinx module. This class  replaces the [ALGNAME] tag in the template with the correct algoritm name and the [DOCUMENTATION] tag with the rst generated for the algorthm and saves the output. 
  

Each of these classes can be run seperately or the class runConverters can be used to run the entire suite. runConverters requires a few paths to be specified so the converter will work: 
```python
algDir = '' #Path to the mantid framework folder
conDir =  '' #Folder where the converted RST files of the algorithms will be saved
conUsageDir = '' #Folder where the converted usage documentents will be saved
tempDir = '' #A temp folder which can be used during the conversion
```
<sub>Note: If running classes individually these paths need to be updated in the __main__ of each class<sub>

##Usage Sections
Usage sections are split off into their own folder and are not included in the main converted rst file for each algorithm. 

##Output of alg2rst
The final output for an algorithm would be this for the LoadFullProfFile algorithm:


    .. algorithm:: LoadLog
    
    .. summary:: LoadLog
    
    .. aliases:: LoadLog
    
    .. usage:: LoadLog
    
    .. properties:: LoadLog
    
    **Parameters Note:** Note that it is possible to use both of the
    optional 'spectrum' properties (i.e. a range and a list) together if so
    desired.
    
    Load ISIS log file(s)
    ~~~~~~~~~~~~~~~~~~~~~
    
    Assumes that a log file originates from a PC (not VMS) environment, i.e.
    the log files to be loaded are assumed to have the extension .txt. Its
    filename is assumed to starts with the raw data file identifier followed
    by the character '\_', and a log file is assumed to have a format of two
    columns, where the first column consists of data-time strings of the ISO
    8601 form and the second column consists of either numbers or strings
    that may contain spaces.
    
    Parent algorithm
    ~~~~~~~~~~~~~~~~
    
    LoadLog is also a child algorithm of `LoadRaw <LoadRaw>`__, i.e. it gets
    called whenever LoadRaw is executed.
    
    Load SNS text log file
    ~~~~~~~~~~~~~~~~~~~~~~
    
    If the file is determined to be a SNS text log file it should be of the
    form
    
    | ``655747325.450625Â Â Â 0.000000Â Â Â Â 24.000000Â Â Â 26.000000Â Â Â 0.000000``
    | ``655747325.716250Â Â Â 0.296875Â Â Â Â 24.000000Â Â Â 26.000000Â Â Â 0.000000``
    | ``655747325.997500Â Â Â 0.593750Â Â Â Â 24.000000Â Â Â 26.000000Â Â Â 0.000000``
    | ``655747326.263125Â Â Â 0.906250Â Â Â Â 24.000000Â Â Â 26.000000Â Â Â 0.000000``
    | ``655747326.544375Â Â Â 1.093750Â Â Â Â 24.000000Â Â Â 26.000000Â Â Â 0.000000``
    | ``655747326.825625Â Â Â 1.406250Â Â Â Â 24.000000Â Â Â 26.000000Â Â Â 0.000000``
    | ``655747327.091250Â Â Â 1.703125Â Â Â Â 24.000000Â Â Â 26.000000Â Â Â 0.000000``
    | ``655747327.372500Â Â Â 2.000000Â Â Â Â 24.000000Â Â Â 26.000000Â Â Â 0.000000``
    | ``655747327.638125Â Â Â 2.203125Â Â Â Â 24.000000Â Â Â 26.000000Â Â Â 0.000000``
    | ``655747327.919375Â Â Â 2.500000Â Â Â Â 24.000000Â Â Â 26.000000Â Â Â 0.000000``
    | ``655747328.200625Â Â Â 2.796875Â Â Â Â 24.000000Â Â Â 26.000000Â Â Â 0.000000``
    | ``655747328.466250Â Â Â 3.093750Â Â Â Â 24.000000Â Â Â 26.000000Â Â Â 0.000000``
    
    The first column is the number of seconds since January 1, 1990, then
    the other columns (space delimited) are the log values. For this mode
    the *name* and *units* parameters must be specified.
    
    .. categories:: LoadLog



The HTML rendering of this can be seen here: 
http://jmccarthy-mantid.github.io/html/_static/LoadLog.html


##Edge Cases
Due to the file size or PanDoc fails to convert the algorithms:
* LoadDectorInfo
* PerformIndexOperations
* PreprocessDetectorsToMD

These need to be converted by hand or by using the online Pandoc converter: http://johnmacfarlane.net/pandoc/try/
