The following utilises `WeightedMean <WeightedMean>`__ and
`WeightedMeanMD <WeightedMeanMD>`__ to inspect the same data.

| ``import math``
| ``# Create some input arrays data``
| ``pi = 3.14``
| ``s1 = []``
| ``e1 = []``
| ``s2 = []``
| ``e2 = []``
| ``extents = [0,40]``
| ``x = range(extents[0], extents[1])``
| ``theta_shift=0.4``
| ``for i in x :``
| ``   theta = 0.02 * i * pi``
| ``   s1.append(math.sin(theta))``
| ``   e1.append(math.sin(theta))``
| ``   s2.append(math.sin(theta+theta_shift))``
| ``   e2.append(math.sin(theta+theta_shift))``
| ``# Create Matrix workspaces from input arrrays``
| ``matrix_1 =CreateWorkspace(DataX=x, DataE=e1, NSpec=1,DataY=s1)``
| ``matrix_2 =CreateWorkspace(DataX=x, DataE=e2, NSpec=1,DataY=s2)``
| ``# Create MD workspaces from input arrays``
| ``md_1 =CreateMDHistoWorkspace(Dimensionality=1,SignalInput=s1,ErrorInput=e1,NumberOfBins=[len(x)],Extents=extents,Names="v",Units="t")``
| ``md_2 =CreateMDHistoWorkspace(Dimensionality=1,SignalInput=s2,ErrorInput=e2,NumberOfBins=[len(x)],Extents=extents,Names="v",Units="t")``
| ``# Produce the weighted mean as a matrix workspace.``
| ``mean = WeightedMean(InputWorkspace1=matrix_1, InputWorkspace2=matrix_2)``
| ``# Produce the weithed mean as a 1D MD workspace. Contents sould be identical to the output created above.``
| ``mean_md = WeightedMeanMD(LHSWorkspace=md_1,RHSWorkspace=md_2)``
