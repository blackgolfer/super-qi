{-# LANGUAGE  TypeFamilies #-}

module Signal.Model
(Sig_0
,Sig_1
,blocks
,Triple
,Sig_3
,oblocks
,Sig
,SigF
) where

import qualified Signal.Utils as Utils
import Signal.Types
import Signal.Padding

type family SigF a where
  SigF a = [a]

type Sig_0 a = SigNum a=>SigF a
type Sig_1 a = SigNum a=>SigF [a]

--type Triple::Type->Type->Type
type Triple a  = ([a],[a],[a])

type Sig_3 a = SigNum a=>SigF (Triple a)

blocks::forall a.SigNum a=>Int->Sig_0 a->Sig_1 a
blocks n x
    | not $ Utils.ispower2 n = error "illegal size of blocks"
    | n<=0 = [x]
blocks _ [] = []
blocks n xs = take n xs:blocks n (drop n xs)

oblocksInner::Int->Sig_1 a->Sig_3 a
oblocksInner n (x:xs)
    | length (take 3 (x : xs))  < 3 = [] -- `take 3` intended to make it work for infinite sequence
    | otherwise = (drop (length x-n) $ head w, w!!1, take n $ last w):oblocksInner n xs
    where
        w=take 3 (x:xs)

oblocks::SigNum a=>PaddingMethod->Int->Sig_1 a->Sig_3 a
oblocks pm n xs
    | (n > length xs) || not (Utils.ispower2 n) = error "illegal size of blocks"
    | pm == PERIODIC = oblocksInner n (last xs : xs ++ [head xs])
    | pm == ZERO = oblocksInner n (replicate n 0:xs ++ [replicate n 0])
    | pm == SYMETRIC = oblocksInner n (reverse (head xs):xs++[reverse $ last xs])
    | otherwise = error "unkown method"

class Sig s where
    transform::(a->a)->s a->s a

instance Sig [] where
    transform=fmap