.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

This algorithm takes a a `MatrixWorkspace <MatrixWorkspace>`__ and
converts it into a `MDEventWorkspace <MDEventWorkspace>`__ that can be
viewed in the `SliceViewer <SliceViewer>`__.

The algorithm currently only works for instruments with
`RectangularDetectors <RectangularDetectors>`__. The coordinates of the
output workspace are:

-  Pixel X coordinate (integer starting at 0)
-  Pixel Y coordinate (integer starting at 0)
-  The center of the bin of the spectrum in that pixel (e.g.
   time-of-flight)

Each MDEvent created has a weight given by the number of counts in that
bin. Zero bins are not converted to events (saving memory).

Once created, the `MDEventWorkspace <MDEventWorkspace>`__ can be viewed
in the `SliceViewer <SliceViewer>`__. It can also be rebinned with
different parameters using `BinMD <BinMD>`__. This allows you to view
the data in detector-space. For example, you might use this feature to
look at your detector's sensitivity as a function of position, as well
as a function of TOF. You can also do line plots of the data. See this
screenshot for example:

.. figure:: images\SliceViewer-DetectorFace.png
   :alt: SliceViewer-DetectorFace.png

   SliceViewer-DetectorFace.png
BankNumbers Parameter
^^^^^^^^^^^^^^^^^^^^^

If your instrument has several
`RectangularDetectors <RectangularDetectors>`__, you can use the
*BankNumbers* property to specify which one(s) to convert. The algorithm
looks for RectangularDetectors with the name 'bankXX' where XX is the
bank number.

If you specify more than one bank number, then the algorithm will create
a 4D MDEventWorkspace. The fourth dimension will be equal to the bank
number, allowing you to easily pick a bank to view.

.. algm_categories::
