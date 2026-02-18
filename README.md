[Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

 # Quaternions

This module provides classes and utilities for working with quaternions — a number system that extends complex numbers to four dimensions. Quaternions are commonly used to represent rotations in 3D space and are valued for their numerical stability and compact representation compared with rotation matrices.

Key features in this folder:

- `quaternion.py`: a pure-Python `Quaternion` class with arithmetic, conjugation, norm, and rotation helpers.
- `quaternion.cpp`: a C++ implementation for performance-sensitive use cases.
- `quaternionic_integer.py`: utilities for quaternionic integer arithmetic.
- `quaternion_numpy.py`: NumPy-style subclasses and interoperability helpers.
- `utils/`: assorted helper functions and tools for quaternion operations.

## Overview
Quaternions have the form a + bi + cj + dk, where a, b, c, d are real numbers and i, j, k satisfy specific multiplication rules. The quaternion algebra is non-commutative but supports division (a division ring).

## Usage
Install any project dependencies and import the module from this package. Example (illustrative):

```python
from quaternion.quaternion import Quaternion

# Construct a quaternion and perform basic operations
q = Quaternion(1, 0, 1, 0)
r = Quaternion(0, 1, 0, 1)
product = q * r
conj = q.conjugate()
norm = q.norm()
```

Refer to the module docstrings and tests for full API details and additional examples.

## Development & Tests
- Run unit tests (from repository root):

```bash
pip install -r requirements.txt
pytest
```

## Contributing
- Bug reports, feature requests, and pull requests are welcome. Please include tests and documentation for new features.

## References
- See standard references on quaternions and rotation mathematics for theory and applications.
