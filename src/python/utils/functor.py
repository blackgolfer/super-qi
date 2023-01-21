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
                rs.append(tmp)
            return Tuple(tuple(rs))
        except Exception as e:
            return EmptyTuple()

    def __iter__(self):
        return iter(self.signal)

    def __len__(self):
        try:
            return len(self.signal)
        except Exception as e:
            pass

    def __getitem__(self,p):
        try:
            return self.signal[p]
        except Exception as e:
            pass

class EmptyTuple(TimeSeries[A]):

    def fmap(self, func: Callable[[A], B]) -> TimeSeries[B]:
        return self
    
    def bind(self, func: Callable[[A], TimeSeries[B]]) -> TimeSeries[B]:
        return self
    
    def __repr__(self):
        return "Empty...."

    def __len__(self):
        pass

    def __getitem__(self,_):
        pass