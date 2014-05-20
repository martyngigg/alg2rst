.. algorithm:: RebinToWorkspace

.. summary:: RebinToWorkspace

.. aliases:: RebinToWorkspace

.. usage:: RebinToWorkspace

.. properties:: RebinToWorkspace

Takes an input workspace and alters the binning so that all it's spectra
match that of the **first spectrum** of the second workspace. This
algorithm simply builds a parameter list that is passed to the
`Rebin <Rebin>`__ algorithm, which actually does the work.

.. categories:: RebinToWorkspace