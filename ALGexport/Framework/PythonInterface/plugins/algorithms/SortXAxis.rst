.. algorithm:: SortXAxis

.. summary:: SortXAxis

.. aliases:: SortXAxis

.. usage:: SortXAxis

.. properties:: SortXAxis

Clones the input `Matrix Workspaces <MatrixWorkspace>`__ and orders the
x-axis in an ascending fashion. Ensures that the y-axis and error data
is sorted in a consistent way with the x-axis.

This algorithm is for use with small workspaces loaded. It is
particularly suitable for reformatting workspaces loaded via
`LoadASCII <LoadASCII>`__. Input workspaces must be a distribution.

.. categories:: SortXAxis