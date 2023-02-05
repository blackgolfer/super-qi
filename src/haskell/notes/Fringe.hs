module Fringe(fringe) where
import Tree(Tree(..))

data Extensions a = Extensions{eLeft::[a], eRight::[a]}

fringe :: Tree a -> [a]   -- A different definition of fringe
fringe (Leaf x) = [x]
fringe (Branch x y) = fringe x