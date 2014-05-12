**Python**

| ``   GEM = LoadEmptyInstrument(Filename="GEM_Definition.xml") # Create test workspace. Normally just use reduced one``
| ``   CreateCalFileByNames("GEM","output.cal","Bank1,Bank2,Module1")``

**C++**

| ``   IAlgorithm* alg = FrameworkManager::Instance().createAlgorithm("LoadEmptyInstrument");``
| ``   alg.setPropertyValue("Filename", "GEM_Definition.xml")``
| ``   alg.execute()``
| ``   IAlgorithm* alg = FrameworkManager::Instance().createAlgorithm("CreateCalFileByNames");``
| ``   alg->setPropertyValue("InstrumentName", "GEM");``
| ``   alg->setPropertyValue("GroupingFileName", "output.cal");``
| ``   alg->setPropertyValue("GroupNames", "Bank1,Bank2,Module1");``
| ``   alg->execute();``
