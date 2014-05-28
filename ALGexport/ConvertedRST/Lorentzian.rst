.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

A Lorentzian function is defined as:

.. raw:: html

   <center>

:math:`\frac{A}{\pi} \left( \frac{\frac{\Gamma}{2}}{(x-x_0)^2 + (\frac{\Gamma}{2})^2}\right)`

.. raw:: html

   </center>

where:

-  A (Amplitude) - Intensity scaling
-  :math:`x_0` (PeakCentre) - centre of peak
-  :math:`\Gamma/2` (HWHM) - half-width at half-maximum

Note that the FWHM (Full Width Half Maximum) equals two times HWHM, and
the integral over the Lorentzian equals the intensity scaling A.

The figure below illustrate this symmetric peakshape function fitted to
a TOF peak:

.. figure:: images\LorentzianWithConstBackground.png
   :alt: LorentzianWithConstBackground.png

   LorentzianWithConstBackground.png

.. algm_categories::
