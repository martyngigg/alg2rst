**Python**

| ``output = Divide("w1","w2")``
| ``w3 = w1 / w2``
| ``w1 /= w2  # Perform "in-place"``
| ``# Using a scalar``
| ``w3 = w1 / 2.5``
| ``w1 /= 2.5  # Perform "in-place"``

| **C++ Within an Algorithm**
| The usage of basic workspace mathematical operations has been
specially simplified for use within algorithms

| ``//w1 and w2 are workspaces``
| ``workspace_sptr output = w1 / w2;``
