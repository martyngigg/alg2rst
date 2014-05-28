.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

This algorithm converts from a `MatrixWorkspace <MatrixWorkspace>`__ (in
detector/time-of-flight space) to a
`MDEventWorkspace <MDEventWorkspace>`__ containing events in reciprocal
space.

The calculations apply only to elastic diffraction experiments. The
conversion can be done either to Q-space in the lab or sample frame, or
to HKL of the crystal.

If the OutputWorkspace does NOT already exist, a default one is created.
In order to define more precisely the parameters of the
`MDEventWorkspace <MDEventWorkspace>`__, use the
`CreateMDWorkspace <CreateMDWorkspace>`__ algorithm first.

Types of Conversion
^^^^^^^^^^^^^^^^^^^

-  **Q (lab frame)**: this calculates the momentum transfer (ki-kf) for
   each event is calculated in the experimental lab frame.
-  **Q (sample frame)**: the goniometer rotation of the sample is taken
   out, to give Q in the frame of the sample. See
   `SetGoniometer <SetGoniometer>`__ to specify the goniometer used in
   the experiment.
-  **HKL**: uses the UB matrix (see `SetUB <SetUB>`__,
   `FindUBUsingFFT <FindUBUsingFFT>`__ and others) to calculate the HKL
   Miller indices of each event.

Lorentz Correction
^^^^^^^^^^^^^^^^^^

If selected, the following Lorentz correction factor is applied on each
event by multiplying its weight by L:

:math:`L = \frac{ sin(\theta)^2 } { \lambda^{4} }`

Where :math:`\theta` is *half* of the neutron scattering angle
(conventionally called :math:`2\theta`). :math:`\lambda` is the neutron
wavelength in *Angstroms*.

This correction is also done by the
`AnvredCorrection <AnvredCorrection>`__ algorithm, and will be set to
false if that algorithm has been run on the input workspace.

OneEventPerBin option
^^^^^^^^^^^^^^^^^^^^^

If you specify *OneEventPerBin*, then the **histogram** representation
of the input workspace is used, with one MDEvent generated for each bin
of the workspace, **including zeros**.

This can be useful in cases where the experimental coverage needs to be
tracked. With one MDEvent for each bin, you can count which regions in
Q-space have been measured. The `SliceViewer <SliceViewer>`__ has an
option to view normalized by number of events. This means that, for
example, areas with overlap from two runs will appear scaled down.

A significant drawback to this is that the output MDEventWorkspace will
be *significantly* larger than the events alone would be. It currently
must be created in physical memory (it cannot yet be cached to disk).
One way to limit the memory used is to limit the OutputExtents to a
smaller region and only convert part of the space.

Also, the `FindPeaksMD <FindPeaksMD>`__ algorithm may not work optimally
because it depends partly on higher density of events causing more
finely split boxes.

If your input is a `Workspace2D <Workspace2D>`__ and you do NOT check
*OneEventPerBin*, then the workspace is converted to an
`EventWorkspace <EventWorkspace>`__ but with no events for empty bins.

Performance Notes
^^^^^^^^^^^^^^^^^

-  8-core Intel Xeon 3.2 GHz computer: measured between 4 and 5.5
   million events per second (100-200 million event workspace).
-  32-core AMD Opteron 2.7 GHz computer: measured between 8 and 9
   million events per second (400-1000 million event workspaces).

.. algm_categories::
