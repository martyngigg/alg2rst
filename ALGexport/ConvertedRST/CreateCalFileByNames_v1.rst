.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

.. figure:: images\InstrumentTree.jpg
   :alt: Instrument Tree

   Instrument Tree
Create a `calibration file <CalFile>`__ for diffraction focusing based
on list of names of the instrument tree.

If a new file name is specified then offsets in the file are all sets to
zero and all detectors are selected. If a valid calibration file already
exists at the location specified by the `GroupingFileName <CalFile>`__
then any existing offsets and selection values will be maintained and
only the grouping values changed.

Detectors not assigned to any group will appear as group 0, i.e. not
included when using AlignDetector or DiffractionFocussing algorithms.

The group number is assigned based on a descent in the instrument tree
assembly. If two assemblies are parented, say Bank1 and module1, and
both assembly names are given in the GroupNames, they will get assigned
different grouping numbers. This allows to isolate a particular
sub-assembly of a particular leaf of the tree.

.. algm_categories::
