{-# LANGUAGE  ConstraintKinds, RankNTypes #-}

module Signal.Padding
(Padding(..)
,Extensions(..)
,PaddingMethod(ZERO,PERIODIC,SYMETRIC)
) where

import Signal.Types

data Extensions a = Extensions{left::[a]
                              ,right::[a]}
instance (Show a)=>Show (Extensions a) where
    show Extensions{left=l,right=r} = "["++ show l ++ "," ++ show r ++ "]" ++ "\n"

class Padding f where
    pad::SigNum a=>f->(Int->[a]->Extensions a)

data PaddingMethod=ZERO|PERIODIC|SYMETRIC deriving(Eq)

type GetExtensions a = SigNum a=>Int->[a]->Extensions a

zero::GetExtensions a
zero n a = Extensions{left=replicate n 0, right=replicate n 0}

symetric::GetExtensions a
symetric n a = Extensions{left=lr,right=rr} where
    lr = reverse $ take n a
    rr = take n $ reverse a

periodic::GetExtensions a
periodic n a = Extensions{left=lr,right=rr} where
    lr = reverse $ take n  $ reverse a
    rr = take n a

instance Padding PaddingMethod where
    pad ZERO = zero
    pad PERIODIC = periodic
    pad SYMETRIC = symetric