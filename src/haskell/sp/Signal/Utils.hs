module Signal.Utils
(ispower2
,linespace
,windowed
) where

import Data.Bits

ispower2::Int->Bool
ispower2 n
    | n<=0 = False
    | otherwise = (n .&. (n-1))==0

linespace :: (Fractional a, Ord a, Integral n)=>a->a->n->[a]
linespace a1 a2 _
    | a2<=a1 = []
linespace a b n
    | n<=0 = []
    | n==1 = [a, b]
linespace a b n = [let dt=(b-a)/fromIntegral(n-1) in a+dt*fromIntegral i | i<-[0..(n-1)]]

-- windowed on list, returning windows with n elements  each
windowed :: Int->[a]->[[a]]
windowed n x
    | n<=1 = [x]
windowed _ [] = []
windowed n (x:xs)
    | length(take n (x:xs))<n = [] -- `take n` makes sure it works on infinite list
    | otherwise = w:windowed n xs
    where w=take n (x:xs)
-- without guarantee each window has n element, then the following works:
-- windowed n x = Data.List.transpose $ take n $ tails x
-- or
-- windowed n x = map (tak n) $ tails x