.. algorithm:: CreateTransmissionWorkspace

.. summary:: CreateTransmissionWorkspace

.. aliases:: CreateTransmissionWorkspace

.. usage:: CreateTransmissionWorkspace

.. properties:: CreateTransmissionWorkspace

Creates a transmission run workspace given one or more TOF workspaces
and the original run Workspace. If two workspaces are provided, then the
workspaces are stitched together using `Stitch1D <Stitch1D>`__.
InputWorkspaces must be in TOF. A single output workspace is generated
with x-units of Wavlength in angstroms.

.. categories:: CreateTransmissionWorkspace