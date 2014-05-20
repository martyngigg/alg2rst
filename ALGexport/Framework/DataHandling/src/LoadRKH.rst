.. algorithm:: LoadRKH

.. summary:: LoadRKH

.. aliases:: LoadRKH

.. usage:: LoadRKH

.. properties:: LoadRKH

Loads the given file in the RKH text format, which can be a file with
three columns of numbers. If the FirstColumnValue is a recognised
`Mantid unit <Unit_Factory>`__ the workspace is created with just one
spectrum. Alteratively if FirstColumnValue is set to 'SpectrumNumber'
then the workspace can have many spectra with the spectrum ID's equal to
the first column in the file.

.. categories:: LoadRKH