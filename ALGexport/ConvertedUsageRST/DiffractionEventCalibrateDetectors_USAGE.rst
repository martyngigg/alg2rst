**Python**

``   DiffractionEventCalibrateDetectors(InputWorkspace=SNAP_4307, Params="1.9308,0.0002,2.1308", LocationOfPeakToOptimize=2.0308, MaxIterations=100, DetCalFilename="./SNAP_4307.DetCal")``

**C++**

| ``   IAlgorithm* alg = FrameworkManager::Instance().createAlgorithm("DiffractionEventCalibrateDetectors");``
| ``   alg->setPropertyValue("InputWorkspace", "SNAP_4111");``
| ``   alg->setPropertyValue("Params", "1.9308,0.0002,2.1308");``
| ``   alg->setPropertyValue("LocationOfPeakToOptimize","2.0308");``
| ``   alg->setPropertyValue("MaxIterations", "100");``
| ``   alg->setPropertyValue("DetCalFilename", "./SNAP_4307.DetCal");``
| ``   alg->execute();``
