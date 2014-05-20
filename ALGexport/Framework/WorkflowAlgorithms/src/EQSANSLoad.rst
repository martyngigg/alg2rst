.. algorithm:: EQSANSLoad

.. summary:: EQSANSLoad

.. aliases:: EQSANSLoad

.. usage:: EQSANSLoad

.. properties:: EQSANSLoad

Workflow algorithm that loads EQSANS event data and applies basic
corrections to the workspace. Those include:

- Moving the detector at its proper position in Z

- Moving the detector according to the beam center

- Correcting the TOF

- Applying TOF cuts

- Gathering meta-data information such as configuration mask and
moderator position

See `SANS
Reduction <http://www.mantidproject.org/Reduction_for_HFIR_SANS>`__
documentation for details.

.. categories:: EQSANSLoad