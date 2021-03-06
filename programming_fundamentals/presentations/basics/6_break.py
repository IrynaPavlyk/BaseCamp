"""
This module describes simple example with `break` in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

# Example.
print("Iteration over loop [0, 10] with a `break` condition, if the number is equal to 3.")
for i in range(10):
    if i == 3:
        break
    print(i)
