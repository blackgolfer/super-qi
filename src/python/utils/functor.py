from typing import TypeVar, Callable, Generic
from collections.abc import Iterable

A=TypeVar("A")
B=TypeVar("B")

class TimeSeries(Generic[A]):
    pass

class Tuple(TimeSeries[tuple[A]]):
    def __init__(self,sig:tuple[A]):
        if sig!=None:
            if not isinstance(sig,tuple):
                raise TypeError("sig must be tuple")
            self.signal=sig

    def fmap(self,func: Callable[[tuple],tuple])->TimeSeries[tuple[A]]:
        try:
            rs=[]
            for i in self.signal:
                tmp = func(i)
                if tmp==None:
                    continue
                if isinstance(tmp,Iterable):
                    rs.append(tmp)
                else:
                    rs.append((tmp,))
            return Tuple(tuple(rs))
        except Exception as e:
            return ()

    def __iter__(self):
        return iter(self.signal)
