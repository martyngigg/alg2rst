.. algorithm:: Lorentzian

.. summary:: Lorentzian

.. aliases:: Lorentzian

.. usage:: Lorentzian

.. properties:: Lorentzian

A Lorentzian function is defined as:

.. raw:: html

   <center>

:math:`\frac{A}{\pi} \left( \frac{\frac{\Gamma}{2}}{(x-x_0)^2 + (\frac{\Gamma}{2})^2}\right)`

.. raw:: html

   </center>

where:

#. A (Amplitude) - Maximum peak height at peak centre
#. :math:`x_0` (PeakCentre) - centre of peak
#. :math:`\Gamma` (HWHM) - half-width at half-maximum

Note that the FWHM (Full Width Half Maximum) equals two times HWHM, and
the integral over the Lorentzian equals 1.

The figure below illustrate this symmetric peakshape function fitted to
a TOF peak:

.. figure:: images\LorentzianWithConstBackground.png
   :alt: LorentzianWithConstBackground.png

   LorentzianWithConstBackground.png

.. categories:: Lorentzian