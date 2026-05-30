module Quaternion 
( Quaternion(..)
, add
, qNegate
, qSubtract
, multiply
, norm
) where

data Quaternion = Quaternion Float Float Float Float deriving (Eq, Show)

add :: Quaternion -> Quaternion -> Quaternion
add (Quaternion s1 i1 j1 k1) (Quaternion s2 i2 j2 k2) = Quaternion (s1+s2) (i1+i2) (j1+j2) (k1+k2)

qNegate :: Quaternion -> Quaternion
qNegate (Quaternion s i j k) = Quaternion (-s) (-i) (-j) (-k)

qSubtract :: Quaternion -> Quaternion -> Quaternion
qSubtract q1 q2 = add q1 (qNegate q2)

multiply :: Quaternion -> Quaternion -> Quaternion
multiply (Quaternion s1 i1 j1 k1) (Quaternion s2 i2 j2 k2) =
    let s = s1*s2 - i1*i2 - j1*j2 - k1*k2
        i = s1*i2 + i1*s2 + j1*k2 - k1*j2
        j = s1*j2 - i1*k2 + j1*s2 + k1*i2
        k = s1*k2 + i1*j2 - j1*i2 + k1*s2
    in Quaternion s i j k

norm :: Quaternion -> Float
norm (Quaternion s i j k) = s^2 + i^2 + j^2 + k^2