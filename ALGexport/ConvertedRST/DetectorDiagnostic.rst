.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

This algorithm is a C++ replacement for the Python diagnostics.diagnose
function located in the scripts/inelastic directory. The algorithm
expects processed workspaces as input just as the other function did.
The main functionality of the algorithm is to determine issues with
detector vanadium runs and mask out bad pixels. The algorithms that are
run on the detector vanadium are FindDetectorsOutsideLimits and
MedianDetectorTest. It also performs a second set of diagnostics on
another detector vanadium run and DetectorEfficiencyVariation on the
two. The algorithm also checks processed sample workspaces (total counts
and background) for bad pixels as well. The total counts workspace is
tested with FindDetectorsOutsideLimits. The background workspace is run
through MedianDetector test. A processed sample workspace can be given
to perform and CreatePSDBleedMask will be run on it.

.. algm_categories::
