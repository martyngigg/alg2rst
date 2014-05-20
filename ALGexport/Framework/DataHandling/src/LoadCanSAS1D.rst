.. algorithm:: LoadCanSAS1D

.. summary:: LoadCanSAS1D

.. aliases:: LoadCanSAS1D

.. usage:: LoadCanSAS1D

.. properties:: LoadCanSAS1D

Loads the given file, which should be in the CanSAS1d format specified
by canSAS 1D Data Formats Working Group schema
http://svn.smallangles.net/svn/canSAS/1dwg/trunk/cansas1d.xsd and
creates output workspace. CANSAS has a Wiki page at
http://www.smallangles.net/wgwiki/index.php/canSAS_Working_Groups

If the file contains mulitple SASentry elements a workspace group will
be created and each SASentry will be one workspace in the group. Loading
multiple SASdata elements is not supported.

.. categories:: LoadCanSAS1D