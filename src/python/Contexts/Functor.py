from typing import TypeVar, Generic, Callable
from collections.abc import Iterable

A=TypeVar("A")
B=TypeVar("B")

class Functor(Generic[A]):
    pass

class ListFunctor(list[A],Functor[A]):

    def fmap(self,f:Callable[[A],B])->Functor[B]:
        return ListFunctor(map(f,self))
    
class TupleFunctor(tuple[A,...],Functor[A]):

    def fmap(self,f:Callable[[A],B])->Functor[B]:
        return TupleFunctor(map(f,self))
