module Main where
import Tree ( Tree(Leaf,Branch), fringe )
import qualified Fringe ( fringe )  

main = do print (fringe (Branch (Leaf 1) (Leaf 2)))
          print (Fringe.fringe (Branch (Leaf 1) (Leaf 2)))