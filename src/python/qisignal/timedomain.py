from typing import List
import btnt
import utils

def qilinespace(v: List[int],ab=[0,1]):
    a,b=ab
    if utils.is_sorted(v):
        N=v[-1]+1
        dt = (b-a)/(N-1)
        return [dt*i for i in v]
    else:
        raise ValueError("not sorted list")

def left_half(t):
    if t==None:
        return None
    n=len(t)
    if not btnt.ispower2(n):
        raise ValueError("input must be power of 2")
    n>>=1
    return t[0:n]

def right_half(t):
    if t==None:
        return None
    n=len(t)
    if not btnt.ispower2(n):
        raise ValueError("input must be power of 2")
    n>>=1
    return t[n:len(t)]

def partition(t: List[int], n: int):
    return btnt.makebtnt(n,t,left_half,right_half)

block=btnt.btnt2btn

