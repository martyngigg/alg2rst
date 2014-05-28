.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

NormaliseToUnity uses `Integration <Integration>`__ to sum up all the X
bins, then sums up the resulting spectra using
`SumSpectra <SumSpectra>`__. Each bin of the input workspace is then
divided by the total sum, regardless of whether a bin was included in
the sum or not. It is thus possible to normalize a workspace so that a
range of X bins and spectra sums to 1. In that case the sum of the whole
workspace will likely not be equal to 1.

.. algm_categories::
