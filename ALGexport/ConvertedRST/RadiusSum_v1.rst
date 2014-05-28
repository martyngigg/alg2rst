.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

RadiusSum sums the counts in rings against radius.

Below, there is an example of the execution of the RadiusSum to a
Workspace2D where the position of the pixels are not associated to
detector positions, but it is derived from the Axes.

.. figure:: images\ExecuteRadiusSum.png 
   :alt:  800px

    800px
The image below shows a visual interpretation for the inputs of the
algorithm

.. figure:: images\RadiusSumInputs.png 
   :alt:  300px

    300px
The Algorithm create **NumBins** rings around the **Centre** point each
one with :math:`width = BinSize` for
:math:`BinSize=\frac{MaxRadius-MinRadius}{NumBins}`.

The algorithm applies a rudimentary calculation to define the bin for
each that each pixel or detector in the `Workspace2D <Workspace2D>`__,
but taking its center point. If the center point belongs to one bin, it
is considered that the whole pixel belongs to the bin. The picture
below, shows what does this means. An ideal solution for RadiusSum is
the left image, while the right image is what is current implemented.

.. figure:: images\RadiusSumSolutions.png 
   :alt:  300px

    300px
Although the images were applied to an image
`Workspace2D <Workspace2D>`__, the image below shows that it is possible
to apply this algorithm to Workspaces attached to instruments.

.. figure:: images\RadiusSumInstrument.png 
   :alt:  800 px

    800 px

.. algm_categories::
