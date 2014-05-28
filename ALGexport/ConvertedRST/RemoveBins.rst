.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

This algorithm removes bins from a workspace. A minimum and maximum X
value to be removed needs to be provided. This can be in a different
unit to the workspace, in which case it is transformed internally.

The treatment of the removed bins is slightly different, depending on
where in the spectrum the bins to be removed lie:

Bins at either end of spectrum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the workspaces has common X binning for all spectra, then the
`CropWorkspace <CropWorkspace>`__ algorithm will be called as a child
algorithm. This will result in the affected bins (which includes the bin
in which the boundary - XMin or XMax - lies) being removed completely,
leading to the output workspace having fewer bins than the input one. In
the case where the X binning varies from spectrum to spectrum, the bin
values will be set to zero regardless of the setting of the
Interpolation property.

Bins in the middle of a spectrum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Interpolation property is applicable to this situation. If it is set
to "Linear" then the bins are set to values calculated from the values
of the bins on either side of the range. If set to "None" then bins
entirely within the range given are set to zero whilst the bins in which
the boundary fall have their values scaled in proportion to the
percentage of the bin's width which falls outside XMin or XMax as
appropriate.

Restrictions on the input workspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  The input workspace must have a unit set
-  The input workspace must contain histogram data

Related Algorithms
------------------

MaskBins
~~~~~~~~

`MaskBins <MaskBins>`__ will set the data in the desired bins to 0 and
importantly also marks those bins as masked, so that further algorithms
should not include this data in their grouping calculations. This is
particularly used for Diffraction Focussing.

.. algm_categories::
