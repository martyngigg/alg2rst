.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

This algorithm appends the spectra of two workspaces together.

The output workspace from this algorithm will be a copy of the first
input workspace, to which the data from the second input workspace will
be appended.

Workspace data members other than the data (e.g. instrument etc.) will
be copied from the first input workspace (but if they're not identical
anyway, then you probably shouldn't be using this algorithm!).

Restrictions on the input workspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For `EventWorkspaces <EventWorkspace>`__, there are no restrictions on
the input workspaces if ValidateInputs=false.

For `Workspace2Ds <Workspace2D>`__, the number of bins must be the same
in both inputs.

If ValidateInputs is selected, then the input workspaces must also:

-  Come from the same instrument
-  Have common units
-  Have common bin boundaries

Spectrum Numbers
^^^^^^^^^^^^^^^^

If there is an overlap in the spectrum numbers of both inputs, then the
output workspace will have its spectrum numbers reset starting at 0 and
increasing by 1 for each spectrum.

See Also
^^^^^^^^

-  `ConjoinWorkspaces <ConjoinWorkspaces>`__ for joining parts of the
   same workspace.

.. algm_categories::
