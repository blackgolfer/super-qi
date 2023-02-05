{-# LANGUAGE  ConstraintKinds #-}

module Signal.Types
(SigNum
) where

type SigNum a = (Num a, Ord a, Show a)