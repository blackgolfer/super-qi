from typing import TypeVar, Generic, Callable, Generator, Iterable, Iterator
from Basic.Monoid import *
from itertools import accumulate
from functools import reduce

A=TypeVar('A')
B=TypeVar('B')

class Foldable(Generic[A]):
    pass

class ListFoldable(list[A],Foldable[A]):
    def foldl(self,f:Callable[[B,A],B],x0:B)->B:
        return foldl(f,x0,self)
    
    def foldr(self,f:Callable[[A,B],B],x0:B)->B:
        return foldr(f,self,x0)

def foldl_r(f:Callable[[B,A],B],x0:B,v:Iterable[A])->Generator[B,None,None]:
    match v:
        case []: yield x0
        case x,*xs: yield from foldl_r(f,f(x0,x),xs)

def foldr_r(f:Callable[[A,B],B],v:Iterable[A],x0:B)->Generator[B,None,None]:
    match v:
        case []: yield x0
        case *xs,x: yield from foldr_r(f,xs,f(x,x0))

def foldl(f:Callable[[B,A],B],x0:B,v:Iterable[A])->B:
    return reduce(f,v,x0)

def foldr(f:Callable[[A,B],B],v:Iterable[A],x0:B)->B:
    return foldl((lambda x,y:f(y,x)),x0,reversed(v))

def scanl(f:Callable[[B,A],B],x0:B,v:Iterable[A])->list[B]:
    return list(accumulate(v,f,initial=x0))[1:]

def scanr(f:Callable[[A,B],B],v:Iterable[A],x0:B)->list[B]:
    return scanl((lambda x,y:f(y,x)),x0,reversed(v))

def scanl_r(f:Callable[[B,A],B],x0:B,v:Iterable[A])->Generator[B,None,None]:
    match v:
        case []: return
        case x,*xs:
            r = f(x0,x)
            yield r
            yield from scanl_r(f,r,xs)

def scanr_r(f:Callable[[A,B],B],v:Iterable[A],x0:B)->Generator[B,None,None]:
    match v:
        case []: return
        case *xs,x:
            r = f(x,x0)
            yield r
            yield from scanr_r(f,xs,r)

@mempty.register(ListFoldable)
def _(a): return ListFoldable([])

@mappend.register(ListFoldable)
def _(a,b): return ListFoldable(a + b)
