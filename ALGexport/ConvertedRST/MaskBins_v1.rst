.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

Masks bins in a workspace. Masked bins should properly be regarded as
having been completely removed from the workspace. Bins falling within
the range given (even partially) are masked, i.e. their data and error
values are set to zero and the bin is added to the list of masked bins.
This range is masked for all spectra in the workspace (though the
workspace does not have to have common X values in all spectra).

At present, although the zeroing of data will obviously be 'seen' by all
downstream algorithms. Only
`DiffractionFocussing <DiffractionFocussing>`__ (version 2) and
`Q1D <Q1D>`__ have been modified to take account of masking. Several
algorithms (e.g. `Rebin <Rebin>`__, `CropWorkspace <CropWorkspace>`__)
have been modified to properly propagate the masking.

Related Algorithms
------------------

RemoveBins
~~~~~~~~~~

`RemoveBins <RemoveBins>`__ can work in several ways, if the bins are at
the edges of the workspace they will be removed, and that will in many
ways act like Masking the bins. If the bins are in the middle of the
workspace then the effect depends on the type of interpolation, but
importantly these bins will continue to influence future algorithms as
opposed to masked bins. For example, with no interpolation
`RemoveBins <RemoveBins>`__ sets the bin values to 0. This 0 values will
be included in the summing performed in DiffractionFocussing, pushing
down the values in that region. MaskBins is more clever. While if you
look at the data, it will appear that it has simply set the values to 0.
It has also set a series of flags inside that mark those bins to not be
included in further claculations. This means that when you Focus the
data these values are simply missed out of the summing that is
performed.

.. algm_categories::
