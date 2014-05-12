Saves the data in a workspace into a file in the NeXus based 'NXSPE'
format.

Restrictions on the input workspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The input workspace must have units of Momentum Transfer ('DeltaE') and
contain histogram data with common binning on all spectra.

Child Algorithms used
^^^^^^^^^^^^^^^^^^^^^

`FindDetectorsPar <FindDetectorsPar>`__ algorithm is used to calculate
detectors parameters from the instrument description.
