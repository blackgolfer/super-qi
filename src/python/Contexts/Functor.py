from __future__ import annotations
from typing import TypeVar, Generic, Callable
import abc
from functools import partial

A = TypeVar('A')
B = TypeVar('B')

class Functor(Generic[A],metaclass=abc.ABCMeta):
    def const(a,b):
        return a
    @abc.abstractmethod
    def fmap(self,f:Callable[[A],B])->Functor[B]:
        ...
    def mrb(self,a): return self.fmap(partial(Functor.const,a))

class ListFunctor(list[A],Functor[A]):
    #def fmap(self,f:Callable[[A],B])->Functor[B]: return ListFunctor(map(f,self))
    def fmap(self,f:Callable[[A],B])->Functor[B]: return ListFunctor((f(x) for x in self))
    
class TupleFunctor(tuple[A,...],Functor[A]):
    def fmap(self,f:Callable[[A],B])->Functor[B]: return TupleFunctor(map(f,self))