module Quaternion 
( Quaternion(..)
, angle
) where

data Quaternion = Quaternion Float Float Float Float deriving (Eq, Show)

instance Num Quaternion where

    (+) :: Quaternion -> Quaternion -> Quaternion
    (Quaternion s1 i1 j1 k1) + (Quaternion s2 i2 j2 k2) = Quaternion (s1+s2) (i1+i2) (j1+j2) (k1+k2)

    negate :: Quaternion -> Quaternion
    negate (Quaternion s i j k) = Quaternion (-s) (-i) (-j) (-k)

    (-) :: Quaternion -> Quaternion -> Quaternion
    q1 - q2 = q1 + negate q2

    abs :: Quaternion -> Quaternion
    abs (Quaternion s i j k) = Quaternion (sqrt (s^2 + i^2 + j^2 + k^2)) 0 0 0

    signum :: Quaternion -> Quaternion
    signum (Quaternion s i j k) = Quaternion (signum s) (signum i) (signum j) (signum k)

    fromInteger :: Integer -> Quaternion
    fromInteger n = Quaternion (fromInteger n) 0 0 0

    (*) :: Quaternion -> Quaternion -> Quaternion
    (Quaternion s1 i1 j1 k1) * (Quaternion s2 i2 j2 k2) =
        let s = s1*s2 - i1*i2 - j1*j2 - k1*k2
            i = s1*i2 + i1*s2 + j1*k2 - k1*j2
            j = s1*j2 - i1*k2 + j1*s2 + k1*i2
            k = s1*k2 + i1*j2 - j1*i2 + k1*s2
        in Quaternion s i j k

-- The angle of rotation associated with the quaternion
angle :: Quaternion -> Float
angle (Quaternion s i j k) = 
    let Quaternion norm _ _ _ = abs (Quaternion s i j k)
    in acos (s / norm)
