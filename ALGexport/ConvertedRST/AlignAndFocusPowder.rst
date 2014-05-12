This is a workflow algorithm that does the bulk of the work for time
focusing diffraction data. This is done by executing several
sub-algorithms as listed below.

#. `RemovePromptPulse <RemovePromptPulse>`__ (event workspace only)
#. `CompressEvents <CompressEvents>`__ (event workspace only)
#. `CropWorkspace <CropWorkspace>`__
#. `MaskDetectors <MaskDetectors>`__
#. `Rebin <Rebin>`__ or `ResampleX <ResampleX>`__ if not d-space binning
#. `AlignDetectors <AlignDetectors>`__
#. If LRef, minwl, or DIFCref are specified:

   #. `ConvertUnits <ConvertUnits>`__ to time-of-flight
   #. `UnwrapSNS <UnwrapSNS>`__
   #. `RemoveLowResTOF <RemoveLowResTOF>`__
   #. `ConvertUnits <ConvertUnits>`__ to d-spacing

#. `Rebin <Rebin>`__ if d-space binning
#. `DiffractionFocussing <DiffractionFocussing>`__
#. `SortEvents <SortEvents>`__ (event workspace only)
#. `EditInstrumentGeometry <EditInstrumentGeometry>`__ (if appropriate)
#. `ConvertUnits <ConvertUnits>`__ to time-of-f

