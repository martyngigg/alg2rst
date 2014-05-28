.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

This algorithm is responsible for normalising data via a given incident
beam parameter. This parameter, IncidentBeamNormalisation, is controlled
from the reduction property manager. It can have the values *None*,
*ByCurrent* or *ByMonitor*. For SNS, monitor workspaces need to be
passed. Parameters in italics are controlled by the `instrument
parameter file (IPF) <InstrumentParameterFile>`__ unless provided to the
algorithm via a property manager. The mappings are given below.

+-----------------------+-----------------+
| Parameter             | IPF Mapping     |
+=======================+=================+
| MonitorIntRangeLow    | norm-mon1-min   |
+-----------------------+-----------------+
| MonitorIntRangeHigh   | norm-mon1-max   |
+-----------------------+-----------------+

Parameters in italics with dashed perimeters are only controllable by
the IPF name given. All underlined parameters are fixed via other input
method. If normalisation is performed, a sample log called
DirectInelasticReductionNormalisedBy is added to the resulting workspace
with the normalisation procedure used.

Workflow
~~~~~~~~

.. figure:: images\DgsPreprocessDataWorkflow.png
   :alt: DgsPreprocessDataWorkflow.png

   DgsPreprocessDataWorkflow.png

.. algm_categories::
