d up two workspaces and mask some data

| ``ws1=Load("GEM38370")``
| ``MaskDetectors(ws1,"100-200")``
| ``ws2=Load("GEM38370")``
| ``MaskDetectors(ws2,"300-400")``
| ``# Extract the masks to Mask Workspaces ``
| ``#this drops the data and just reatains the mask informantion``
| ``#You can still visualize these using the instrument view``
| ``#Note: ExtractMasking outputs two items you need to catch them seperately``
| ``mw1,detList1=ExtractMasking(ws1)``
| ``mw2,detList2=ExtractMasking(ws2)``
| ``#combine the masks``
| ``#Two ways to do this``
| ``#either``
| ``combinedMask = mw1+mw2``
| ``#or``
| ``MaskDetectors(Workspace=mw1,MaskedWorkspace=mw2)``
| ``#Extract the Mask to a cal file``
| ``dataDir = "C:/MantidInstall/data/"``
| ``MaskWorkspaceToCalFile(combinedMask,dataDir+"mask.cal")``
| `` ``
| ``#Merge this with another cal file to pick up offsets and groups``
| ``MergeCalFiles(UpdateFile = dataDir+"mask.cal", MasterFile=dataDir+"offsets_2006_cycle064.cal", \``
| ``OutputFile=dataDir+"resultCal.cal", MergeOffsets=False, MergeSelections=True,MergeGroups=False)``
