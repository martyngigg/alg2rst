This algorithm performs `Le Bail Fit <Le Bail Fit>`__ to powder
diffraction data, and also supports pattern calculation. This algorithm
will refine a specified set of the powder instrumental profile
parameters with a previous refined background model.

Peak profile function for fit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is the list of the peak profile function supported by this
algorithm.

-  Thermal neutron back-to-back exponential convoluted with pseudo-voigt

   -  geometry-related parameters: Dtt1, Zero, Dtt1t, Dtt2t, Width,
      Tcross
   -  back-to-back exponential parameters: Alph0, Alph1, Beta0, Beta1,
      Alph0t, Alph1t, Beta0t, Beta1t
   -  pseudo-voigt parameters: Sig0, Sig1, Sig2, Gam0, Gam1, Gam2

Optimization
~~~~~~~~~~~~

*LeBailFit* supports regular minimizes in GSL library and a tailored
simulated annealing optimizer.

It is very difficult to achieve reasonable good result by non-linear
minimizers such as Simplex or Levenber-Marquardt, because the parameters

The experience to use non-linear minimizes such as Simplex or

Background
~~~~~~~~~~

This algorithm does not refine background. It takes a previous refined
background model, for instance, from ProcessBackground().

Background fitting is not included in LeBailFit() because the
mathematics problem is not well-defined as peak heights are calculated
but not refined but highly correlated to background model.

Further Information
~~~~~~~~~~~~~~~~~~~

See `Le Bail Fit <Le Bail Fit>`__.
