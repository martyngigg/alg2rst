Python
^^^^^^

Given the variable number and types of possible arguments that Load can
take, its simple Python function cannot just list the properties as
arguments like the others do. Instead the Python function ``Load`` can
handle any number of arguments. The OutputWorkspace and Filename
arguments are the exceptions in that they are always checked for. A
snippet regarding usage from the ``help(Load)`` is shown below

.. raw:: html

   <div style="border:1pt dashed blue; background:#f9f9f9;padding: 1em 0;">

.. code:: python

    # Simple usage, ISIS NeXus file
    Load('INSTR00001000.nxs', OutputWorkspace='run_ws')

    # ISIS NeXus with SpectrumMin and SpectrumMax = 1
    Load('INSTR00001000.nxs', OutputWorkspace='run_ws', SpectrumMin=1, SpectrumMax=1)

    # SNS Event NeXus with precount on
    Load('INSTR_1000_event.nxs', OutputWorkspace='event_ws', Precount=True)

    # A mix of keyword and non-keyword is also possible
    Load(OutputWorkspace='event_ws', Filename='INSTR_1000_event.nxs', Precount=True)

.. raw:: html

   </div>

Loading Multiple Files
^^^^^^^^^^^^^^^^^^^^^^

Loading multiple files is also possible with ``Load``, as well as
workspace addition. For more information, see
`MultiFileLoading <MultiFileLoading>`__.
