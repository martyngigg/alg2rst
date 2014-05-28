.. algorithm::

.. summary::

.. alias::

.. properties::

Description
-----------

Multiply two `MDHistoWorkspace <MDHistoWorkspace>`__'s or a
MDHistoWorkspace and a scalar.

The error of :math:`f = a * b` is propagated with
:math:`df^2 = f^2 * (da^2 / a^2 + db^2 / b^2)`

-  **MDHistoWorkspace \* MDHistoWorkspace**

   -  The operation is performed element-by-element.

-  **MDHistoWorkspace \* Scalar** or **Scalar \* MDHistoWorkspace**

   -  Every element of the MDHistoWorkspace is multiplied by the scalar.

-  **`MDEventWorkspace <MDEventWorkspace>`__'s**

   -  This operation is not supported, as it is not clear what its
      meaning would be.

.. algm_categories::
