'''Defines Quaternion class'''

from __future__ import absolute_import
from __future__ import division
from __future__ import annotations

from numbers import Number, Complex, Real
import re
import math
from collections.abc import Mapping, Iterable
from typing import Union
from dataclasses import dataclass


@dataclass(frozen=True)
class Quaternion(Number):
    '''A quaternion is a number in a four-dimensional mathematical system.
    It can be described as the sum of a scalar and a three-dimensional vector.
    '''

    scalar: float = 0.0
    i:      float = 0.0
    j:      float = 0.0
    k:      float = 0.0

    @classmethod
    def from_string(cls, string: str) -> Quaternion:

        scalar, i, j, k = 0.0, 0.0, 0.0, 0.0

        try:

            if re.search(r"[^\dijk+-.\s]", string):
                raise ValueError

            for x in re.findall(r"[+-]?\s*\d*[.]?\d*[ijk]?\w", string):
                if x[-1] == 'i':
                    i = float(re.sub(r'\s', '', x[:-1]))
                elif x[-1] == 'j':
                    j = float(re.sub(r'\s', '', x[:-1]))
                elif x[-1] == 'k':
                    k = float(re.sub(r'\s', '', x[:-1]))
                else:
                    scalar = float(x.replace(' ', ''))

        except ValueError as exc:
            raise ValueError(
                f'{cls.__name__} arg is a malformed string'
            ) from exc

        return cls(scalar, i, j, k)

    def __repr__(self) -> str:

        i_sign = '-' if self.i < 0 else '+'
        j_sign = '-' if self.j < 0 else '+'
        k_sign = '-' if self.k < 0 else '+'

        scalar_part = f'{self.scalar:.4f}'
        i_part = f'{i_sign} {abs(self.i):.4f}i'
        j_part = f'{j_sign} {abs(self.j):.4f}j'
        k_part = f'{k_sign} {abs(self.k):.4f}k'

        return ' '.join([scalar_part, i_part, j_part, k_part])

    def __add__(self, other: Quaternion) -> Quaternion:
        if isinstance(other, Real):
            s = self.scalar + float(other)
            i = self.i
            j = self.j
            k = self.k
        elif isinstance(other, Complex):
            s = self.scalar + float(other.real)
            i = self.i + float(other.imag)
            j = self.j
            k = self.k
        elif isinstance(other, Quaternion):
            s = self.scalar + other.scalar
            i = self.i + other.i
            j = self.j + other.j
            k = self.k + other.k
        else:
            return NotImplemented
        return Quaternion(s, i, j, k)

    def __radd__(self, other: Quaternion) -> Quaternion:
        if isinstance(other, Real):
            s = float(other) + self.scalar
            i = self.i
            j = self.j
            k = self.k
        elif isinstance(other, Complex):
            s = float(other.real) + self.scalar
            i = float(other.imag) + self.i
            j = self.j
            k = self.k
        else:
            return NotImplemented
        return Quaternion(s, i, j, k)

    def __neg__(self) -> Quaternion:
        return Quaternion(-self.scalar, -self.i, -self.j, -self.k)

    def __pos__(self) -> Quaternion:
        return self

    def __sub__(self, other: Quaternion) -> Quaternion:
        return self + -other

    def __rsub__(self, other: Quaternion) -> Quaternion:
        return -self + other

    def __mul__(self, other: Quaternion) -> Quaternion:
        if isinstance(other, Real):
            s = self.scalar * float(other)
            i = self.i * float(other)
            j = self.j * float(other)
            k = self.k * float(other)
        elif isinstance(other, Complex):
            s = self.scalar * float(other.real) - self.i * float(other.imag)
            i = self.scalar * float(other.imag) + self.i * float(other.real)
            j = self.j * float(other.real) + self.k * float(other.imag)
            k = -self.j * float(other.imag) + self.k * float(other.real)
        elif isinstance(other, Quaternion):
            s = self.scalar * other.scalar - self.i * other.i - self.j * other.j - self.k * other.k
            i = self.scalar * other.i + self.i * other.scalar + self.j * other.k - self.k * other.j
            j = self.scalar * other.j - self.i * other.k + self.j * other.scalar + self.k * other.i
            k = self.scalar * other.k + self.i * other.j - self.j * other.i + self.k * other.scalar
        else:
            return NotImplemented
        return Quaternion(s, i, j, k)

    def __rmul__(self, other: Quaternion) -> Quaternion:
        if isinstance(other, Real):
            s = float(other) * self.scalar
            i = float(other) * self.i
            j = float(other) * self.j
            k = float(other) * self.k
        elif isinstance(other, Complex):
            s = float(other.real) * self.scalar - float(other.imag) * self.i
            i = float(other.real) * self.i + float(other.imag) * self.scalar
            j = float(other.real) * self.j - float(other.imag) * self.k
            k = float(other.real) * self.k + float(other.imag) * self.j
        else:
            return NotImplemented
        return Quaternion(s, i, j, k)

    def __truediv__(self, other: Quaternion) -> Quaternion:
        if isinstance(other, Real):
            return Quaternion(
                self.scalar / float(other),
                self.i / float(other),
                self.j / float(other),
                self.k / float(other)
            )
        if isinstance(other, Complex):
            return self / Quaternion(float(other.real), float(other.imag))
        if isinstance(other, Quaternion):
            return self * other.reciprocal()
        return NotImplemented

    def __rtruediv__(self, other: Union[float, Real, Complex, Quaternion]) -> Quaternion:
        if isinstance(other, Complex):
            return Quaternion(float(other.real), float(other.imag)) * self.reciprocal()
        return NotImplemented

    def __pow__(self, exponent: Union[float, Real, Complex, Quaternion]):
        if isinstance(exponent, Real):
            a = self.norm() ** float(exponent)
            b = math.cos(float(exponent) * self.angle())
            c = self.unit_vector() * math.sin(float(exponent) * self.angle())
            return a * (b + c)
        return NotImplemented

    def __rpow__(self, base: Union[float, Real, Complex, Quaternion]) -> Quaternion:
        if isinstance(base, Real):
            a = math.exp(self.scalar)
            b = math.cos(self.vector().norm())
            c = self.unit_vector() * math.sin(self.vector().norm())
            return (a * (b + c)) ** math.log(float(base))
        return NotImplemented

    def __abs__(self) -> float:
        return self.norm()

    def vector(self) -> Quaternion:
        '''The quaternion's vector component'''
        return Quaternion(0, self.i, self.j, self.k)

    def norm(self) -> float:
        '''The "length" of the quaternion'''
        return math.sqrt(self.scalar ** 2 + self.i ** 2 + self.j ** 2 + self.k ** 2)

    def conjugate(self) -> Quaternion:
        '''The conjugate of the quaternion,
        with the same scalar component and the vector numbers negated
        '''
        return Quaternion(self.scalar, -self.i, -self.j, -self.k)

    def reciprocal(self) -> Quaternion:
        '''The multiplicative inverse of the quaternion'''
        return self.conjugate() / (self.norm() ** 2)

    def unit(self) -> Quaternion:
        '''The unit quaternion is the quaternion divided by its norm'''
        if self == 0:
            return self
        return self / self.norm()

    def angle(self) -> float:
        '''The angle of rotation associated with the quaternion,
        equal to the arccosine of its scalar component divided by its norm
        '''
        return math.acos(self.scalar / self.norm())

    def unit_vector(self) -> Quaternion:
        '''The unit vector associated with the quaternion's vector component,
        representing the axis of rotation
        '''
        return self.vector().unit()

    def complex_pair(self) -> tuple[complex, complex]:
        '''The quaternion as a 2-tuple of complex numbers'''
        return (complex(self.scalar, self.i), complex(self.j, self.k))

    def __complex__(self) -> complex:
        return complex(self.scalar, self.i)

    def __float__(self) -> float:
        return float(self.scalar)

    def __int__(self) -> int:
        return int(self.scalar)

    def __bool__(self) -> bool:
        return self != 0

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Real):
            if self.scalar == other \
            and self.i == 0 \
            and self.j == 0 \
            and self.k == 0:
                return True
        elif isinstance(other, Complex):
            if self.scalar == other.real \
            and self.i == other.imag \
            and self.j == 0 \
            and self.k == 0:
                return True
        elif isinstance(other, Quaternion):
            if self.scalar == other.scalar \
            and self.i == other.i \
            and self.j == other.j \
            and self.k == other.k:
                return True
        return False

    def __ne__(self, other: object) -> bool:
        return not self == other

    def to_list(self) -> list[Union[float, Real]]:
        '''The quaternion components as a list'''
        return [self.scalar, self.i, self.j, self.k]

    def vector_to_list(self) -> list[Union[float, Real]]:
        '''The quaternion vector components as a list'''
        return [self.i, self.j, self.k]

    def __hash__(self) -> int:
        if not self.j and not self.k:
            if not self.i:
                return hash(self.scalar)
            return hash(complex(self.scalar, self.i))
        return hash((self.scalar, self.i, self.j, self.k))

    @classmethod
    def from_iterable(cls, it) -> Quaternion:
        '''Create a quaternion instance from an iterable'''
        if isinstance(it, Mapping):
            return cls(**it)
        if isinstance(it, Iterable):
            return cls(*it)
        raise TypeError(f'{cls.__name__}.from_iterable() argument must be an iterable')

Quaternion.register(Complex)
