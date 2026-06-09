'''Defines QuaternionicInteger class'''

from __future__ import absolute_import

from numbers import Integral, Complex, Real
from quaternion import Quaternion

class QuaternionicInteger(Quaternion):

    '''Analogous to the Gaussian integers for complex numbers,
    quaternionic integers are quaternions with integer coefficients.
    '''

    def __post_init__(self):
        object.__setattr__(self, 'scalar', int(self.scalar))
        object.__setattr__(self, 'i', int(self.i))
        object.__setattr__(self, 'j', int(self.j))
        object.__setattr__(self, 'k', int(self.k))

    def __repr__(self):

        i_sign = '-' if self.i < 0 else '+'
        j_sign = '-' if self.j < 0 else '+'
        k_sign = '-' if self.k < 0 else '+'

        i_part = f'{i_sign} {abs(self.i)}i'
        j_part = f'{j_sign} {abs(self.j)}j'
        k_part = f'{k_sign} {abs(self.k)}k'

        return ' '.join([str(self.scalar), i_part, j_part, k_part])

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Integral):
            return self == QuaternionicInteger(int(other), 0, 0, 0)
        if isinstance(other, Complex):
            return (self.scalar == other.real and
                    self.i == other.imag and
                    self.j == 0 and
                    self.k == 0)
        if isinstance(other, Real):
            return (self.scalar == float(other) and
                    self.i == 0 and
                    self.j == 0 and
                    self.k == 0)
        if isinstance(other, QuaternionicInteger):
            return (self.scalar == other.scalar and
                    self.i == other.i and
                    self.j == other.j and
                    self.k == other.k)
        if isinstance(other, Quaternion):
            return (self.scalar == other.scalar and
                    self.i == other.i and
                    self.j == other.j and
                    self.k == other.k)
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.scalar, self.i, self.j, self.k))

    def __add__(self, other):
        from numbers import Real, Complex
        if isinstance(other, Integral):
            return QuaternionicInteger(self.scalar + int(other), self.i, self.j, self.k)
        if isinstance(other, QuaternionicInteger):
            return QuaternionicInteger(self.scalar + other.scalar,
                                       self.i + other.i,
                                       self.j + other.j,
                                       self.k + other.k)
        if isinstance(other, Complex):
            return Quaternion(self.scalar + float(other.real), self.i + float(other.imag), self.j, self.k)
        if isinstance(other, Quaternion):
            return Quaternion(self.scalar + other.scalar,
                              self.i + other.i,
                              self.j + other.j,
                              self.k + other.k)
        if isinstance(other, Real):
            return Quaternion(self.scalar + float(other), self.i, self.j, self.k)
        return NotImplemented

    def __radd__(self, other):
        from numbers import Real, Complex
        if isinstance(other, Integral):
            return QuaternionicInteger(int(other) + self.scalar, self.i, self.j, self.k)
        if isinstance(other, QuaternionicInteger):
            return QuaternionicInteger(other.scalar + self.scalar,
                                       other.i + self.i,
                                       other.j + self.j,
                                       other.k + self.k)
        if isinstance(other, Complex):
            return Quaternion(float(other.real) + self.scalar, float(other.imag) + self.i, self.j, self.k)
        if isinstance(other, Quaternion):
            return Quaternion(other.scalar + self.scalar,
                              other.i + self.i,
                              other.j + self.j,
                              other.k + self.k)
        if isinstance(other, Real):
            return Quaternion(float(other) + self.scalar, self.i, self.j, self.k)
        return NotImplemented

    def __neg__(self):
        return QuaternionicInteger(-self.scalar, -self.i, -self.j, -self.k)

    def __mul__(self, other):
        from numbers import Real, Complex
        if isinstance(other, Integral):
            return QuaternionicInteger(self.scalar * int(other), self.i * int(other), self.j * int(other), self.k * int(other))
        if isinstance(other, QuaternionicInteger):
            s = self.scalar * other.scalar - self.i * other.i - self.j * other.j - self.k * other.k
            i = self.scalar * other.i + self.i * other.scalar + self.j * other.k - self.k * other.j
            j = self.scalar * other.j - self.i * other.k + self.j * other.scalar + self.k * other.i
            k = self.scalar * other.k + self.i * other.j - self.j * other.i + self.k * other.scalar
            return QuaternionicInteger(s, i, j, k)
        if isinstance(other, Complex):
            return super().__mul__(Quaternion(float(other.real), float(other.imag)))
        if isinstance(other, Quaternion):
            return super().__mul__(other)
        if isinstance(other, Real):
            return super().__mul__(float(other))
        return NotImplemented

    def __rmul__(self, other):
        from numbers import Real, Complex
        if isinstance(other, Integral):
            return QuaternionicInteger(int(other) * self.scalar, int(other) * self.i, int(other) * self.j, int(other) * self.k)
        if isinstance(other, QuaternionicInteger):
            s = other.scalar * self.scalar - other.i * self.i - other.j * self.j - other.k * self.k
            i = other.scalar * self.i + other.i * self.scalar + other.j * self.k - other.k * self.j
            j = other.scalar * self.j - other.i * self.k + other.j * self.scalar + other.k * self.i
            k = other.scalar * self.k + other.i * self.j - other.j * self.i + other.k * self.scalar
            return QuaternionicInteger(s, i, j, k)
        if isinstance(other, Complex):
            return Quaternion(float(other.real), float(other.imag)) * Quaternion(self.scalar, self.i, self.j, self.k)
        if isinstance(other, Quaternion):
            return other * Quaternion(self.scalar, self.i, self.j, self.k)
        if isinstance(other, Real):
            return float(other) * Quaternion(self.scalar, self.i, self.j, self.k)
        return NotImplemented

    def __truediv__(self, other):
        from numbers import Real, Complex
        if isinstance(other, Integral):
            # exact integer division -> return QuaternionicInteger
            s = self.scalar / int(other)
            i = self.i / int(other)
            j = self.j / int(other)
            k = self.k / int(other)
            if all(float(x).is_integer() for x in (s, i, j, k)):
                return QuaternionicInteger(int(s), int(i), int(j), int(k))
            return Quaternion(s, i, j, k)
        if isinstance(other, Quaternion) or isinstance(other, Complex) or isinstance(other, Real):
            return super().__truediv__(other)
        return NotImplemented

    def __rtruediv__(self, other):
        from numbers import Real, Complex
        if isinstance(other, Integral):
            return Quaternion(float(other)) / Quaternion(self.scalar, self.i, self.j, self.k)
        if isinstance(other, Quaternion) or isinstance(other, Complex) or isinstance(other, Real):
            return Quaternion(other) / Quaternion(self.scalar, self.i, self.j, self.k)
        return NotImplemented

    def conjugate(self):
        return QuaternionicInteger(self.scalar, -self.i, -self.j, -self.k)

QuaternionicInteger.register(Integral) # type: ignore[type-abstract]
