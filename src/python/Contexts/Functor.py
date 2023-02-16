from __future__ import annotations
from typing import TypeVar, Generic, Callable
import abc
from Basic.Monoid import *
from itertools import chain

A = TypeVar('A')
B = TypeVar('B')

class Functor(Generic[A],metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fmap(self,f:Callable[[A],B])->Functor[B]:
        ...
    def const(a,_): return a
    def lconst(self,a): return (lambda _: a)
    #def mrb(self,a): return self.fmap(partial(Functor.const,a))
    def mrb(self,a): return self.fmap(self.lconst(a))

class ListFunctor(list[A],Functor[A],metaclass=abc.ABCMeta):
    def fmap(self,f:Callable[[A],B])->Functor[B]: return ListFunctor(map(f,self))

@mempty.register(ListFunctor)
def _(a): return ListFunctor([])

@mappend.register(ListFunctor)
def _(a,b): return ListFunctor(a + b)

@mconcat.register(ListFunctor)
def _(a): return ListFunctor(chain.from_iterable(a))

class TupleFunctor(tuple[A,...],Functor[A]):
    def fmap(self,f:Callable[[A],B])->Functor[B]: return TupleFunctor(map(f,self))
