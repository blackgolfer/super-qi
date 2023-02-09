from Signal.Utils import ispower2
from Signal.Types import signum, sig_0, sig_1, sig_3
from Signal.Padding import PaddingMethodNames
from Contexts.Foldable import scanl, scanr
from functools import partial

def blocks(n:int,s:sig_0)->sig_1:
    if not ispower2(n): raise ValueError("block size must be power of 2")
    elif s==[]: return []
    elif n<=0 or n>len(s): return [s,]
    else: return [s[:n],]+blocks(n,s[n:]) # [take(n,s),]+blocks(n,drop(n,s))

def getExtensions(pmn:PaddingMethodNames,n:int,s:sig_1)->(sig_0,sig_0):
    match pmn:
        case PaddingMethodNames.ZERO: return ([0]*n,[0]*n)
        case PaddingMethodNames.PERIODIC: return (s[-1][-n:],s[0][:n])
        case PaddingMethodNames.SYMETRIC: return (s[0][:n][::-1],s[-1][-n:][::-1])
        case _: raise ValueError("unknown method")

def leftEdge(n,acc,x): return (acc[1][-n:],x)
def rightEdge(n,x,acc): return x+(acc[1][:n],)

def oblocks(pmn:PaddingMethodNames,n:int,s:sig_1)->sig_3:
    if not ispower2(n): raise ValueError("block size must be power of 2")
    elif s==[]: return [] 
    elif n<=0 or n>len(s[0]): ValueError("illegal extension length")
    else:
        l2=partial(leftEdge,n)
        r2=partial(rightEdge,n)
        exts = getExtensions(pmn,n,s)
        left = ([],exts[0]) # initial value for the scanl, also defines the shape of the element for output
        right = ([],exts[1],[]) # initial value for the scanr, defining the shape of the final output list
        tmp=list(scanl(l2,left,s))
        return sig_3(scanr(r2,tmp,right))[::-1]