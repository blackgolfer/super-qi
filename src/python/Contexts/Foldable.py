from typing import TypeVar, Generic, Callable, Generator, Iterable
from Basic.Monoid import *

A=TypeVar('A')
B=TypeVar('B')

class Foldable(Generic[A]):
    pass

class ListFoldable(list[A],Foldable[A]):
    def foldl(self,f:Callable[[B,A],B],x0:B)->B:
        return next(foldl(f,x0,self))
    
    def foldr(self,f:Callable[[A,B],B],x0:B)->B:
        return next(foldr(f,self,x0))

def foldl(f:Callable[[B,A],B],x0:B,v:Iterable[A])->Generator[B,None,None]:
    match v:
        case []: yield x0
        case x,*xs: yield from foldl(f,f(x0,x),xs)
    
def foldr(f:Callable[[A,B],B],v:Iterable[A],x0:B)->Generator[B,None,None]:
    match v:
        case []: yield x0
        case *xs,x: yield from foldr(f,xs,f(x,x0))

def scanl(f:Callable[[B,A],B],x0:B,v:Iterable[A])->Generator[B,None,None]:
    match v:
        case []: return
        case x,*xs:
            r = f(x0,x)
            yield r
            yield from scanl(f,r,xs)

def scanr(f:Callable[[A,B],B],v:Iterable[A],x0:B)->Generator[B,None,None]:
    match v:
        case []: return
        case *xs,x:
            r = f(x,x0)
            yield r
            yield from scanr(f,xs,r)

@mempty.register(ListFoldable)
def _(a): return ListFoldable([])

@mappend.register(ListFoldable)
def _(a,b): return ListFoldable(a + b)
