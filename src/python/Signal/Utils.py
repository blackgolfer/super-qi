#import more_itertools
from typing import TypeVar, Sequence, Generator
A=TypeVar("A")

def ispower2(n:int)->bool:
    return (n & (n-1) == 0) and n != 0

def linespace(a:float,b:float,N:int)->list[float]:
    if N<=0 or b<a: raise ValueError("Illegal input")
    if b==a: return []
    else:
        dt=(b-a)/float(N-1)
        return [a+dt*i for i in range(N)]

#windowed = more_itertools.windowed # windowed(v:[a],n:int) instead of windowed(n:int,v:[a])

def windowed(n:int,v:Sequence[A])->Generator[Sequence[A],None,None]:
    if v:
        if len(v[:n])<n: return
        else:
            yield v[:n]
            yield from windowed(n,v[1:])
    else: return