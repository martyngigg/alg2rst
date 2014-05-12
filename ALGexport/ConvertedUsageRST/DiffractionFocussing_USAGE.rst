**Python**

``   OutWS = DiffractionFocussing("InWS","filename")``

**C++**

| ``   IAlgorithm* alg = FrameworkManager::Instance().createAlgorithm("DiffractionFocussing");``
| ``   alg->setPropertyValue("InputWorkspace", "InWS"); ``
| ``   alg->setPropertyValue("OutputWorkspace", "OutWS");    ``
| ``   alg->setPropertyValue("GroupingFileName", "filename");``
| ``   alg->execute();``
| ``   Workspace* ws = FrameworkManager::Instance().getWorkspace("OutWS");``
