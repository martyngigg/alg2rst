.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

| Slow moving (low energy and long wavelength neutrons) maybe detected
after the end of the frame in which they entered the experimental
apparatus. A schematic example of this is shown below where the neutrons
are marked as circles.
| |Schematic diagram of neutrons entering an instrument and being
detected\|centre\||
| The two neutons on the right of the diagram were actually produced in
frame 1 but will be recorded in frame 2 at low time of flight (TOF) and
a straight `ConvertUnits <ConvertUnits>`__ will bin them at high energy
and short wavelength! `UnwrapSNS <UnwrapSNS>`__ moves those particles to
the end of the spectrum by increasing their time of flight by the
duration of a frame multiplied by the number (one or more) of frames
they were "late" by.

To assess if it is impossible for a particle to have arrived in the same
frame it was detected a maximum speed for particles is calculated based
on LRef and Tmin. The algorithm then calculates the mean speed of all
detected particles and corrects those whose speed was greater than the
maximum.

Normally LRef is the total length of the flight path from the source
(particle location when t=0) to a detector. For event data, if the
detector with the shortest flight path was chosen it maybe possible to
leave the Tmin empty and so that a first particle arrival time is used.
Otherwise the Tmin should be set to < the arrival time of the fastest
neutron at the given detector.

If Tmin was set either Tmax or DataFrameWidth must be set to ensure the
frame duration calculated correctly. If Tmax was set the frame width is
the difference between Tmax and Tmin. DataFrameWidth overrides this and
the width is the difference between the longest and shortest TOFs in the
data.

.. |Schematic diagram of neutrons entering an instrument and being detected\|centre\|| image:: UnwrapSNS_inst.png

.. algm_categories::
