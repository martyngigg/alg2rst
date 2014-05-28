.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

Given a PeaksWorkspace and a set of lattice parameters, attempts to tag
each peak with a HKL value by comparing d-spacings between potential HKL
matches and the peaks as well as angles between Q vectors.

Usage Notes
-----------

This algorithm does not generate a UB Matrix, it will only index peaks.
Run CalculateUMatrix algorithm after executing this algorithm in order
to attach a UB Matrix onto the sample. The CopySample algorithm will
allow this UB Matrix to be transfered between workspaces.

.. algm_categories::
