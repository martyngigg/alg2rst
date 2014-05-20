.. algorithm:: MonitorLiveData

.. summary:: MonitorLiveData

.. aliases:: MonitorLiveData

.. usage:: MonitorLiveData

.. properties:: MonitorLiveData

The MonitorLiveData algorithm is started in the background by
`StartLiveData <StartLiveData>`__ and repeatedly calls
`LoadLiveData <LoadLiveData>`__. **It should not be necessary to call
MonitorLiveData directly.**

This algorithm simply calls `LoadLiveData <LoadLiveData>`__ at the given
*UpdateFrequency*. For more details, see
`StartLiveData <StartLiveData>`__.

For details on the way to specify the data processing steps, see:
`LoadLiveData <LoadLiveData#Description>`__.

.. categories:: MonitorLiveData