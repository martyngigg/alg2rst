Prerequisites
~~~~~~~~~~~~~

The workspace spectrum axis should be converted to signed\_theta using
`ConvertSpectrumAxis <ConvertSpectrumAxis>`__ and the x axis should be
converted to Wavelength using `ConvertUnits <ConvertUnits>`__ before
running this algorithm. Histogram input workspaces are expected.

The algorithm will looks for a specific log value called *stheta*, which
contains the incident theta angle :math:`theta_i`. If the input
workspace does not contain this value, or if you wish to override this
value you can do so by providing your own *IncidentTheta* property and
enabling *OverrideIncidentTheta*.

Transformations
~~~~~~~~~~~~~~~

Output workspaces are always 2D MD Histogram workspaces, but the
algorithm will perform one of three possible transformations.

-  Convert to :math:`Q_x`, :math:`Q_z`
-  Convert to :math:`K_i`, :math:`K_f`
-  Convert to :math:`P_i-P_f`, :math:`P_i+P_f`. Note that P and K are
   interchangeable.

where

:math:`Q_x = \frac{2\pi}{\lambda}(sin\theta_f + sin\theta_i)`

:math:`Q_z = \frac{2\pi}{\lambda}(cos\theta_f - cos\theta_i)`

:math:`K_i = \frac{2\pi}{\lambda}sin\theta_i`

:math:`K_f = \frac{2\pi}{\lambda}sin\theta_f`

.. raw:: mediawiki

   {{AlgorithmLinks|ConvertToReflectometryQ}}

After Transformation
~~~~~~~~~~~~~~~~~~~~

You will usually want to rebin using `BinMD <BinMD>`__ or
`SliceMD <SliceMD>`__ after transformation because the output workspaces
are not regularly binned.
