.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

Clones the input `Matrix Workspaces <MatrixWorkspace>`__ and orders the
x-axis in an ascending fashion. Ensures that the y-axis and error data
is sorted in a consistent way with the x-axis. All x-values of the input
workspace MUST be in either a descending or ascending fashion before
passing to this algorithm.

This algorithm is for use with small workspaces loaded. It is
particularly suitable for reformatting workspaces loaded via
`LoadASCII <LoadASCII>`__. Input workspaces must be a distribution.

.. algm_categories::
