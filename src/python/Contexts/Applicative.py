from typing import TypeVar, Generic, Callable, Iterable, Generator
from Contexts.Functor import ListFunctor
from Basic.Monoid import *

A=TypeVar('A')
B=TypeVar('B')
C=TypeVar('C')

class Applicative(Generic[A]):
    pass

class ListApplicative(ListFunctor[A],Applicative[A]):
    def pure(self,x:A)->Applicative[A]:
        return ListApplicative([x])
    def ap(self,fs:list[Callable[[A],B]])->Applicative[B]:
        return ListApplicative((f(x) for f in fs for x in self))
    def liftA2(self,f:Callable[[A,B],C],ys:list[B])->Applicative[C]: 
        return ListApplicative((f(x,y) for x in self for y in ys))
    def then(self,ys:list[B])->Applicative[B]:
        return ListApplicative((y for _ in self for y in ys))

def liftA2(f:Callable[[A,B],C],xs:Iterable[A],ys:Iterable[B])->Generator[C,None,None]:
    return (f(x,y) for x in xs for y in ys)

def ap(fs:list[Callable[[A],B]],xs:list[A])->ListApplicative[B]:
    return ListApplicative((f(x) for f in fs for x in xs))

def pure(i:A)->ListApplicative[A]:
    return ListApplicative([i])

@mempty.register(ListApplicative)
def _(a): return ListApplicative([])

@mappend.register(ListApplicative)
def _(a,b): return ListApplicative(a + b)
