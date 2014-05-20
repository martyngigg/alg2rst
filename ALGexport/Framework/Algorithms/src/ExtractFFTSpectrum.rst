.. algorithm:: ExtractFFTSpectrum

.. summary:: ExtractFFTSpectrum

.. aliases:: ExtractFFTSpectrum

.. usage:: ExtractFFTSpectrum

.. properties:: ExtractFFTSpectrum

This algorithm iterates the `FFT <FFT>`__ algorithm on each spectrum of
InputWorkspace, computing the Fourier Transform and storing the
transformed spectrum in OutputWorkspace. If InputImagWorkspace is also
passed, then the pair spectrum *i* of InputWorkspace (real) and spectrum
*i* of InputImagWorkspace (real) are taken together as spectrum *i* of a
complex workspace, on which `FFT <FFT>`__ is applied.

The FFTPart parameter specifies which transform is selected from the
output of the `FFT <FFT>`__ algorithm:

For the case of input containing real and imaginary workspaces:

+-----------+------------------------------+
| FFTPart   | Description                  |
+===========+==============================+
| 0         | Complete real part           |
+-----------+------------------------------+
| 1         | Complete imaginary part      |
+-----------+------------------------------+
| 2         | Complete transform modulus   |
+-----------+------------------------------+

For the case of input containing no imaginary workspace:

+-----------+----------------------------------------+
| FFTPart   | Description                            |
+===========+========================================+
| 0         | Real part, positive frequencies        |
+-----------+----------------------------------------+
| 1         | Imaginary part, positive frequencies   |
+-----------+----------------------------------------+
| 2         | Modulus, positive frequencies          |
+-----------+----------------------------------------+
| 3         | Complete real part                     |
+-----------+----------------------------------------+
| 4         | Complete imaginary part                |
+-----------+----------------------------------------+
| 5         | Complete transform modulus             |
+-----------+----------------------------------------+

.. categories:: ExtractFFTSpectrum