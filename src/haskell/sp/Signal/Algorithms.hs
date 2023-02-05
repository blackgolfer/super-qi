module Signal.Algorithms
(decimation
) where

decimation::Int->[a]->[a]
decimation n x
    | n<2 = x
decimation _ [] = []
decimation n (x:xs) = x:decimation n (drop (n-1) xs)