.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

Bin-by-bin mode
~~~~~~~~~~~~~~~

In this, the default scenario, each spectrum in the workspace is
normalised on a bin-by-bin basis by the monitor spectrum given. The
error on the monitor spectrum is taken into account. The normalisation
scheme used is:

:math:`(s_i)_{Norm}=(\frac{s_i}{m_i})*\Delta w_i*\frac{\sum_i{m_i}}{\sum_i(\Delta w_i)}`

where :math:`s_i` is the signal in a bin, :math:`m_i` the count in the
corresponding monitor bin, :math:`\Delta w_i` the bin width,
:math:`\sum_i{m_i}` the integrated monitor count and
:math:`\sum_i{\Delta w_i}` the sum of the monitor bin widths. In words,
this means that after normalisation each bin is multiplied by the bin
width and the total monitor count integrated over the entire frame, and
then divided by the total frame width. This leads to a normalised
histogram which has unit of counts, as before.

If the workspace does not have common binning, then the monitor spectrum
is rebinned internally to match each data spectrum prior to doing the
normalisation.

Normalisation by integrated count mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This mode is used if one or both of the relevant 'IntegrationRange'
optional parameters are set. If either is set to a value outside the
workspace range, then it will be reset to the frame minimum or maximum,
as appropriate.

The error on the integrated monitor spectrum is taken into account in
the normalisation. No adjustment of the overall normalisation takes
place, meaning that the output values in the output workspace are
technically dimensionless.

Restrictions on the input workspace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The data must be histogram, non-distribution data.

Child Algorithms used
~~~~~~~~~~~~~~~~~~~~~

The `ExtractSingleSpectrum <ExtractSingleSpectrum>`__ algorithm is used
to pull out the monitor spectrum if it's part of the InputWorkspace or
MonitorWorkspace. For the 'integrated range' option, the
`Integration <Integration>`__ algorithm is used to integrate the monitor
spectrum.

In both cases, the `Divide <Divide>`__ algorithm is used to perform the
normalisation.

.. algm_categories::
