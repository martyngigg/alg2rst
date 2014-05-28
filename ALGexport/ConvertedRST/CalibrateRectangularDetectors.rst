.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

Here are examples of input and output from PG3 and SNAP:

.. figure:: images\PG3_Calibrate.png
   :alt: PG3_Calibrate.png

   PG3\_Calibrate.png
.. figure:: images\SNAP_Calibrate.png
   :alt: SNAP_Calibrate.png

   SNAP\_Calibrate.png
-The purpose of this algorithm is to calibrate the detector pixels and
write a calibration file. The calibration file name contains the
instrument, run number, and date of calibration. A binary Dspacemap file
that converts from TOF to d-space including the calculated offsets is
also an output option. For CrossCorrelation option: If one peak is not
in the spectra of all the detectors, you can specify the first n
detectors to be calibrated with one peak and the next n detectors to be
calibrated with the second peak. If a color fill plot of the calibrated
workspace does not look good, do a color fill plot of the workspace that
ends in cc to see if the CrossCorrelationPoints and/or PeakHalfWidth
should be increased or decreased. Also plot the reference spectra from
the cc workspace.

.. algm_categories::
