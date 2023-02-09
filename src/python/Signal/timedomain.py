from typing import List
from Signal.btnt import btn, makebtnt, btnt2btn
from Signal.Utils import ispower2

def left_half(t:List[int])->List[int]:
    if t==None:
        return []
    n=len(t)
    if not ispower2(n):
        raise ValueError("input must be power of 2")
    n>>=1
    return t[0:n]

def right_half(t:List[int])->List[int]:
    if t==None:
        return []
    n=len(t)
    if not ispower2(n):
        raise ValueError("input must be power of 2")
    n>>=1
    return t[n:len(t)]

def partition(t:List[int], n:int)->btn:
    return makebtnt(n,t,left_half,right_half)

block=btnt2btn

