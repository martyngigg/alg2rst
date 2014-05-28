.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

The algorithm LoadNexusProcessed will read a Nexus data file created by
`SaveNexusProcessed <SaveNexusProcessed>`__ and place the data into the
named workspace. The file name can be an absolute or relative path and
should have the extension .nxs, .nx5 or .xml. Warning - using XML format
can be extremely slow for large data sets and generate very large files.
The optional parameters can be used to control which spectra are loaded
into the workspace (not yet implemented). If spectrum\_min and
spectrum\_max are given, then only that range to data will be loaded.

A Mantid Nexus file may contain several workspace entries each labelled
with an integer starting at 1. By default the highest number workspace
is read, earlier ones can be accessed by setting the EntryNumber.

If the saved data has a reference to an XML file defining instrument
geometry this will be read.

Time series data
~~~~~~~~~~~~~~~~

The log data in the Nexus file (NX\_LOG sections) is loaded as
TimeSeriesProperty data within the workspace. Time is stored as seconds
from the Unix epoch. Only floating point logs are stored and loaded at
present.

Child algorithms used
~~~~~~~~~~~~~~~~~~~~~

The Child Algorithms used by LoadMuonNexus are:

-  LoadInstrument - this algorithm looks for an XML description of the
   instrument and if found reads it.

.. algm_categories::
