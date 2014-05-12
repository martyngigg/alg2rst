Stitches single histogram `Matrix Workspaces <MatrixWorkspace>`__
together outputing a stitched Matrix Workspace. This algorithm is a
wrapper over `Stitch1DMD <Stitch1DMD>`__.

The algorithm expects pairs of StartOverlaps and EndOverlaps values. The
order in which these are provided determines the pairing. There should
be N entries in each of these StartOverlaps and EndOverlaps lists, where
N = 1 -(No of workspaces to stitch). StartOverlaps and EndOverlaps are
in the same units as the X-axis for the workspace.

The workspaces must be histogrammed. Use
`ConvertToHistogram <ConvertToHistogram>`__ on workspaces prior to
passing them to this algorithm.
