.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

Saves the geometry information of the detectors in a workspace into a
PHX format ASCII file. The angular positions and angular sizes of the
detectors are calculated using `FindDetectorsPar <FindDetectorsPar>`__
algorithm.

Mantid generated PHX file is an ASCII file consisting of the header and
7 text columns. Header contains the number of the rows in the phx file
excluding the header. (number of detectors). The column has the
following information about a detector:

| `` *         1st column      secondary flightpath,e.g. sample to detector distance (m) -- Mantid specific``
| `` *         2nt  "          0``
| `` *         3rd  "          scattering angle (deg)``
| `` *         4th  "          azimuthal angle (deg)``
| `` *                        (west bank = 0 deg, north bank = 90 deg etc.)``
| `` *                        (Note the reversed sign convention wrt ``\ ```.par`` <SavePAR>`__\ `` files)``
| `` *         5th  "          angular width e.g. delta scattered angle (deg) ``
| `` *         6th  "          angular height e.g. delta azimuthal angle (deg)``
| `` *         7th  "          detector ID    -- Mantid specific. ``
| `` *---``

In standard phx file only the columns 3,4,5 and 6 contain useful
information. You can expect to find column 1 to be the secondary
flightpath and the column 7 -- the detector ID in Mantid-generated phx
files only.

.. algm_categories::
