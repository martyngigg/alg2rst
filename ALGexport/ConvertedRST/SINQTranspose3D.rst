Description
-----------

SINQTranspose3D is an algorithm which fixes some problems with SINQ
data. This algorithm is probably not generally useful. It basically
reorders the data in a 3D MDHistoWorkspace. The following reordering
options are available:

Y,X,Z
    Swaps X and Y in the data
X,Z,Y
    Swaps Y and Z in the data
TRICS
    Swaps from C to Fortran storage order
AMOR
    Converts storage order and swaps X and Y

