#ifndef QUATERNIONS_CPP
#define QUATERNIONS_CPP

#include "quaternion.hpp"

Quaternion::Quaternion(double s0, double i0, double j0, double k0)
{
    scalar = s0; i = i0; j = j0; k = k0;
}

Quaternion::~Quaternion() {}

void Quaternion::SetVals(double s0, double i0, double j0, double k0)
{
    scalar = s0; i = i0; j = j0; k = k0;
}

// add Quaternions
Quaternion Quaternion::operator+(const Quaternion & rhs)
{
    return Quaternion(scalar + rhs.scalar, i + rhs.i, j + rhs.j, k + rhs.k);
}

// right scalar addition
Quaternion Quaternion::operator+(const double n) {
    return Quaternion(scalar + n, i, j, k);
}

// right complex addition
Quaternion Quaternion::operator+(const complex<double> n) {
    return Quaternion(scalar + n.real(), i + n.imag(), j, k);
}

// subtract Quaternions
Quaternion Quaternion::operator-(const Quaternion & rhs)
{
    return Quaternion(scalar - rhs.scalar, i - rhs.i, j - rhs.j, k - rhs.k);
}

// right scalar subtraction
Quaternion Quaternion::operator-(const double n) {
    return Quaternion(scalar - n, i, j, k);
}

// right complex subtraction
Quaternion Quaternion::operator-(const complex<double> n) {
    return Quaternion(scalar - n.real(), i - n.imag(), j, k);
}

// negate Quaternion
Quaternion Quaternion::operator-()
{
    return Quaternion(-scalar, -i, -j, -k);
}

// Hamilton multiplication of two Quaternions
Quaternion Quaternion::operator*(const Quaternion & rhs)
{
    double a = scalar*rhs.scalar - i*rhs.i - j*rhs.j - k*rhs.k;
    double b = scalar*rhs.i + i*rhs.scalar + j*rhs.k - k*rhs.j;
    double c = scalar*rhs.j - i*rhs.k + j*rhs.scalar + k*rhs.i;
    double d = scalar*rhs.k + i*rhs.j - j*rhs.i + k*rhs.scalar;
    return Quaternion(a, b, c, d);
}

// right scalar multiplication
Quaternion Quaternion::operator*(const double n)
{
    return Quaternion(n*scalar, n*i, n*j, n*k);
}

// right complex multiplication
Quaternion Quaternion::operator*(const complex<double> n)
{
    Quaternion nq = Quaternion(n.real(), n.imag(), 0, 0);
    return *this * nq;
}
/*
 // left complex multiplication
 friend Quaternion Quaternion::operator*(complex<double> n, Quaternion & q)
 {
 Quaternion nq = Quaternion(n.real(), n.imag(), 0, 0);
 return nq * q;
 }
 */
// right scalar division
Quaternion Quaternion::operator/(const double n)
{
    return Quaternion(scalar/n, i/n, j/n, k/n);
}

// right complex division
Quaternion Quaternion::operator/(const complex<double> n)
{
    Quaternion nq = Quaternion(n.real(), n.imag(), 0, 0);
    return *this / nq;
}
/*
 // left complex division
 friend Quaternion Quaternion::operator/(complex<double> n, Quaternion & q)
 {
 Quaternion nq = Quaternion(n.real(), n.imag(), 0, 0);
 return nq / q;
 }
 */
Quaternion Quaternion::Conjugate()
{
    return Quaternion(scalar, -i, -j, -k);
}

double Quaternion::Norm()
{
    return sqrt(scalar*scalar + i*i + j*j + k*k);
}

Quaternion Quaternion::Reciprocal()
{
    return this->Conjugate() / pow(this->Norm(), 2);
}

Quaternion Quaternion::operator/(const Quaternion & rhs)
{
    Quaternion q = rhs;
    return *this * q.Reciprocal();
}

Quaternion Quaternion::operator+=(const Quaternion & rhs)
{
    *this = *this + rhs;
    return *this;
}

Quaternion Quaternion::operator*=(const Quaternion & rhs)
{
    *this = *this * rhs;
    return *this;
}

Quaternion Quaternion::operator-=(const Quaternion & rhs)
{
    *this = *this - rhs;
    return *this;
}

Quaternion Quaternion::operator/=(const Quaternion & rhs)
{
    *this = *this / rhs;
    return *this;
}

Quaternion Quaternion::operator+=(const double n)
{
    *this = *this + n;
    return *this;
}

Quaternion Quaternion::operator*=(const double n)
{
    *this = *this * n;
    return *this;
}

Quaternion Quaternion::operator-=(const double n)
{
    *this = *this - n;
    return *this;
}

Quaternion Quaternion::operator/=(const double n)
{
    *this = *this / n;
    return *this;
}

// displays Quaternion in s +/- xi +/- yj +/- zk form
string Quaternion::QDisplay()
{
    ostringstream oss;
    string i_sign = (i < 0 ? "-" : "+");
    string j_sign = (j < 0 ? "-" : "+");
    string k_sign = (k < 0 ? "-" : "+");
    oss << scalar;
    if (i != 0) oss << " " << i_sign << " " << abs(i) << "i";
    if (j != 0) oss << " " << j_sign << " " << abs(j) << "j";
    if (k != 0) oss << " " << k_sign << " " << abs(k) << "k";
    return oss.str();
}

// displays Quaternion's vector component
string Quaternion::Vect()
{
    ostringstream oss;
    string j_sign = (j < 0 ? "-" : "+");
    string k_sign = (k < 0 ? "-" : "+");
    if (i != 0) {
        oss << i << "i";
        if (j != 0) oss << " " << j_sign << " " << abs(j) << "j";
        if (k != 0) oss << " " << k_sign << " " << abs(k) << "k";
    }
    else {
        if (j != 0) {
            oss << j << "j";
            if (k != 0) oss << " " << k_sign << " " << abs(k) << "k";
        }
        else {
            if (k != 0) oss << k << "k";
            else oss << 0;
        }
    }
    return oss.str();
}

// displays quaternion in s +/- xi +/- yj +/- zk form
// including zero vals
string Quaternion::QDisplayZeros()
{
    ostringstream oss;
    string i_sign = (i < 0 ? "-" : "+");
    string j_sign = (j < 0 ? "-" : "+");
    string k_sign = (k < 0 ? "-" : "+");
    oss << scalar
    << " " << i_sign << " " << abs(i) << "i"
    << " " << j_sign << " " << abs(j) << "j"
    << " " << k_sign << " " << abs(k) << "k";
    return oss.str();
}

// overload power function for quaterntions
Quaternion pow(const Quaternion & q0, int n){
    Quaternion q(1, 0, 0, 0);
    for (int i = 0; i < n; i++) q *= q0;
    return q;
}

// outputs quaternion in s +/- xi +/- yj +/- zk form
ostream& operator<<(ostream& oss, Quaternion& q) {
    string i_sign = (q.i < 0 ? "-" : "+");
    string j_sign = (q.j < 0 ? "-" : "+");
    string k_sign = (q.k < 0 ? "-" : "+");
    oss << q.scalar
    << " " << i_sign << " " << abs(q.i) << "i"
    << " " << j_sign << " " << abs(q.j) << "j"
    << " " << k_sign << " " << abs(q.k) << "k";
    return oss;
}

#endif
