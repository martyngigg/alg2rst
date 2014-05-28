.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

This algorithm uses a numerical integration method to calculate
attenuation factors resulting from absorption and single scattering in a
flat plate (slab) sample with the dimensions and material properties
given. Factors are calculated for each spectrum (i.e. detector position)
and wavelength point, as defined by the input workspace. The sample is
divided up into cuboids having sides of as close to the size given in
the ElementSize property as the sample dimensions will allow. Thus the
calculation speed depends linearly on the total number of bins in the
workspace and goes as :math:`\rm{ElementSize}^{-3}`.

Path lengths through the sample are then calculated for the centre-point
of each element and a numerical integration is carried out using these
path lengths over the volume elements.

Restrictions on the input workspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The input workspace must have units of wavelength. The
`instrument <instrument>`__ associated with the workspace must be fully
defined because detector, source & sample position are needed.

.. algm_categories::
