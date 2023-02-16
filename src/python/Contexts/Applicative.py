from __future__ import annotations
from typing import TypeVar, Generic, Callable, Iterable, Generator
import abc
from Contexts.Functor import Functor, ListFunctor
from Basic.Monoid import *
from functools import singledispatch
from itertools import chain

A=TypeVar('A')
B=TypeVar('B')
C=TypeVar('C')

class Applicative(Functor[A],metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def pure(self,x:A)->Applicative[A]:
        ...
    @abc.abstractmethod
    def ap(self,fs:list[Callable[[A],B]])->Applicative[B]:
        ...
    @abc.abstractmethod
    def liftA2(self,f:Callable[[A,B],C],ys:list[B])->Applicative[C]:
        ...
    @abc.abstractmethod
    def then(self,ys:list[B])->Applicative[B]:
        ...

class ListApplicative(ListFunctor[A],Applicative[A]):
    def pure(self,x:A)->Applicative[A]:
        return ListApplicative([x])
    def ap(self,fs:ListApplicative[Callable[[A],B]])->Applicative[B]:
        return ListApplicative([f(x) for f in fs for x in self])
    def liftA2(self,f:Callable[[A,B],C],ys:ListApplicative[B])->Applicative[C]: 
        return ListApplicative([f(x,y) for x in self for y in ys])
    def then(self,ys:ListApplicative[B])->Applicative[B]:
        return ListApplicative([y for _ in self for y in ys])

def liftA2(f:Callable[[A,B],C],xs:Iterable[A],ys:Iterable[B])->Generator[C,None,None]:
    return (f(x,y) for x in xs for y in ys)

@singledispatch
def ap(a,b): raise NotImplementedError("Not implemented for "+a)

@singledispatch
def pure(a): raise NotImplementedError("not implemented for "+a)

@ap.register(list)
def _(a,b): return ListApplicative([f(x) for f in a for x in b])

@pure.register(list)
def _(i): return mconcat(ListApplicative([i]))

@mempty.register(ListApplicative)
def _(a): return ListApplicative([])

@mappend.register(ListApplicative)
def _(a,b): return ListApplicative(a + b)

@mconcat.register(ListApplicative)
def _(a): return ListApplicative(chain.from_iterable(a))