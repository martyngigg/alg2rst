.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

This algorithm fits a bivariate normal distribution( plus background) to
the data on each time slice. The Fit program uses
`BivariateNormal <BivariateNormal>`__ for the Fit Function.

The area used for the fitting is calculated based on the dQ parameter. A
good value for dQ is 1/largest unit cell length. This parameter dictates
the size of the area used to approximate the intensity of the peak. The
estimate .1667/ max(a,b,c) assumes \|Q\|=1/d.

The result is returned in this algorithm's output "Intensity" and
"SigmaIntensity" properties. The peak object is NOT CHANGED.

The table workspace is also a result. Each line contains information on
the fit for each good time slice. The column names( and information) in
the table are:

| `` Time, Channel, Background, Intensity, Mcol, Mrow, SScol,SSrow, SSrc, NCells,``
| `` ChiSqrOverDOF, TotIntensity, BackgroundError, FitIntensityError, ISAWIntensity,``
| ``  ISAWIntensityError,TotalBoundary, NBoundaryCells, Start Row, End Row,Start Col, and End Col.``
| ``  The last column has a comma separated List of sepctral ID's used in the time slice.``

The final Peak intensity is the sum of the IsawIntensity for each time
slice. The error is the square root of the sum of squares of the
IsawIntensityError values.

The columns whose names are Background, Intensity, Mcol, Mrow, SScol,
SSrow, and SSrc correspond to the parameters for the BivariateNormal
curve fitting function.

This algorithm has been carefully tweaked to give good results for
interior peaks only. Peaks close to the edge of the detector may not
give good results.

This Algorithm is also used by the `PeakIntegration <PeakIntegration>`__
algorithm when the Fit tag is selected.

.. algm_categories::
