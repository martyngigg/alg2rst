#alg2rst


Mantid MediaWiki Algorithms to RST 

This converter is designed for a single use to extract the documentation from Mantid algorithms and convert them to RST. It can also remove the documentation from the Mantid CCP files. 

##Requirments
alg2rst requires Pandoc to be installed and available on the command line. Install instructions for Pandoc can be found here: http://johnmacfarlane.net/pandoc/installing.html

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
<sub>Note: If running classes individually these paths need to be updated in the __main__ of each class<sub>

##Usage Sections
Usage sections are split off into their own folder and are not included in the main converted rst file for each algorithm. 

##Output of alg2rst
The final output for an algorithm would be this for the LoadLog algorithm:

```
.. algorithm:: LoadFullprofFile

.. summary:: LoadFullprofFile

.. aliases:: LoadFullprofFile

.. usage:: LoadFullprofFile

.. properties:: LoadFullprofFile

This algorithm is to import Fullprof .irf file (peak parameters) and
.hkl file (reflections) and record the information to TableWorkspaces,
which serve as the inputs for algorithm LeBailFit.

Format of Instrument parameter TableWorkspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Instrument parameter TableWorkspace contains all the peak profile
parameters imported from Fullprof .irf file.

Presently these are the peak profiles supported

``*Â ThermalÂ neutronÂ backÂ toÂ backÂ exponentialÂ convolutedÂ withÂ pseudo-voigtÂ (profileÂ No.Â 10Â inÂ Fullprof)``

Each row in TableWorkspace corresponds to one profile parameter.

Columns include Name, Value, FitOrTie, Min, Max and StepSize.

Format of reflection TableWorkspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each row of this workspace corresponds to one diffraction peak. The
information contains the peak's Miller index and (local) peak profile
parameters of this peak. For instance of a back-to-back exponential
convoluted with Gaussian peak, the peak profile parameters include
Alpha, Beta, Sigma, centre and height.

How to use algorithm with other algorithms
------------------------------------------

This algorithm is designed to work with other algorithms to do Le Bail
fit. The introduction can be found in the wiki page of
`LeBailFit <LeBailFit>`__.

.. categories:: LoadFullprofFile
```

The HTML rendering of this can be seen here: 
http://jmccarthy-mantid.github.io/html/_static/LoadLog.html
