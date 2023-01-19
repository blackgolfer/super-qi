from collections import namedtuple
from collections.abc import Iterable
from itertools import islice

Interval=namedtuple("Interval",["least","zero","final"])
Ball=namedtuple("Ball",["center","radius"])

class qislice:
    def __init__(self,i:Interval,period):
        if not isinstance(i.least,int) or not isinstance(i.final,int) or not isinstance(period,int):
            raise ValueError("Invalid type input in intervel constructor")
        if i.final<0 or period<0 or (i.least<0 and i.final>period):
            raise ValueError("invalid inputs")
        self.interval=i
        self.period=period

    def __call__(self,data: Iterable):
        if self.interval.least<0:
            return data[self.interval.least:]+data[:self.interval.final]
        elif self.interval.final>self.period:
            return data[self.interval.least:]+data[:(self.interval.final%self.period)]
        else:
            return data[self.interval.least:self.interval.final]

    def __repr__(self) -> str:
        return f"{self.interval}, period({self.period})"

    def shift(self, n: int):
        i=Interval(self.interval.least+n,self.interval.zero
                    +n,self.interval.final+n)
        return qislice(i,self.period)

    def shift_generator(self,n,N):
        if not isinstance(n,int) or not isinstance(N,int):
            raise TypeError("inputs must be integer")
        return iter([self.shift(n*i) for i in range(N)])

