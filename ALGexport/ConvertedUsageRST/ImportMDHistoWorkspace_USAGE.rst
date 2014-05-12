The following call will create an MDHistoWorkspace called *demo* with 3
dimensions with 2 bins in each dimension. Each dimension will span from
-1 to 1 in units of T.

``ImportMDHistoWorkspace(Filename='demo.txt',Dimensionality='3',Extents='-1,1,-1,1,-1,1',NumberOfBins='2,2,2',Names='A,B,C',Units='T,T,T',OutputWorkspace='demo')``

And here's the corresponding contents of *demo.txt*:

| ``1  1.1``
| ``2  2.1``
| ``3  3.1``
| ``4  4.1``
| ``5  5.1``
| ``6  6.1``
| ``7  7.1``
| ``8  8.1``
