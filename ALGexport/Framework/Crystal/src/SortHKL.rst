.. algorithm:: SortHKL

.. summary:: SortHKL

.. aliases:: SortHKL

.. usage:: SortHKL

.. properties:: SortHKL

Peaks are sorted first by H, then K, and then L. For equivalent HKL in
the point group, the intensity is averaged and all the equivalent HKLs
have the same average intensity. Outliers with zscore > 3 from each
group of equivalent HKLs are not included in the average.

.. categories:: SortHKL