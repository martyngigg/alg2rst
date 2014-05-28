.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

The algorithm creates a new 2D workspace containing the first maxima
(minima) for each spectrum, as well as their X boundaries and error.
This is used in particular for single crystal as a quick way to find
strong peaks. By default, the algorithm returns the maxima.

The `Max <Max>`__ and `Min <Min>`__ algorithms are just calls to the
`MaxMin <MaxMin>`__ algorithm, with the ShowMin flag set to true/false
respectively.

.. algm_categories::
