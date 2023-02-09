from typing import TypeVar, Generic, Callable
from Contexts.Applicative import ListApplicative
from Basic.Monoid import *

A=TypeVar('A')
B=TypeVar('B')

class Monad(Generic[A]):
    pass

class ListMonad(ListApplicative[A],Monad[A]):

    def bind(self,f:Callable[[A],list[B]])->Monad[B]:
        return ListMonad([y for x in self for y in f(x)]) # basically it is a map and flatten

@mempty.register(ListMonad)
def _(a): return ListMonad([])

@mappend.register(ListMonad)
def _(a,b): return ListMonad(a + b)
