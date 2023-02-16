from __future__ import annotations
from typing import TypeVar, Generic, Callable
import abc
from Contexts.Applicative import Applicative, ListApplicative
from Basic.Monoid import *
from itertools import chain

A=TypeVar('A')
B=TypeVar('B')

class Monad(Applicative[A],metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def bind(self,f:Callable[[A],Monad[B]])->Monad[B]:
        ...
    @abc.abstractmethod
    def mreturn(a:A)->Monad[A]:
        ...
    @abc.abstractmethod
    def fail(_)->Monad[A]:
        ...

class ListMonad(ListApplicative[A],Monad[A]):
    # bind=mconcat.fmap
    def bind(self,f:Callable[[A],ListMonad[B]])->Monad[B]:
        return ListMonad([y for x in self for y in f(x)]) # basically it is a map and flatten
    def mreturn(a:A)->Monad[A]: return ListMonad([a])
    def fail(_): return ListMonad([])

@singledispatch
def ap(a,b): raise NotImplementedError("Not implemented for "+a)

@singledispatch
def pure(a): raise NotImplementedError("not implemented for "+a)

@ap.register(list)
def _(a,b): return ListMonad((f(x) for f in a for x in b))

@pure.register(list)
def _(i): return mconcat(ListMonad([i]))

@mempty.register(ListMonad)
def _(a): return ListMonad([])

@mappend.register(ListMonad)
def _(a,b): return ListMonad(a + b)

@mconcat.register(ListMonad)
def _(a): return ListMonad(chain.from_iterable(a))

class MonadPlus(Monad[A],metaclass=abc.ABCMeta):
    @abc.abstractstaticmethod
    def mone()->Monad:
        ...
    @abc.abstractstaticmethod
    def mzero()->Monad:
        ...
    @abc.abstractstaticmethod
    def mplus(a:Monad[A],b:Monad[A])->Monad[A]:
        ...
    @staticmethod
    def guard(a:bool)->Monad:
        if a: return MonadPlus.mone()
        else: return MonadPlus.mzero()

class ListMonadPlus(ListMonad[A],MonadPlus[A]):
    @staticmethod
    def mone() -> Monad: return ListMonadPlus([None])
    @staticmethod
    def mzero()->Monad: return ListMonad([])
    @staticmethod
    def mplus(a:Monad[A],b:Monad[A])->Monad[A]: return mconcat(a,b)
    