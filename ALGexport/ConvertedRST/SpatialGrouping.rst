.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

This algorithm creates an XML Grouping file of the form:

.. raw:: html

   <div style="border:1pt dashed black; background:#f9f9f9;padding: 1em 0;">

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" ?>
    <detector-grouping> 
    <group name="fwd"><detids val="1,2,17,32"/></group> 
    <group name="bwd"><detids val="33,36,38,60,64"/> </group>   
    </detector-grouping>

.. raw:: html

   </div>

Based on information retrieved from the `Nearest
Neighbours <Nearest Neighbours>`__ class in Mantid Geometry.

.. algm_categories::
