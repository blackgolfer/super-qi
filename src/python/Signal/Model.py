from typing import TypeVar, Callable, Iterable
from Contexts.Functor import ListFunctor

from Signal.Types import SigNum,Sig_0, Sig_1, Sig_3

A = TypeVar("A")
B = TypeVar("B")

def blocks(n:int,s:Sig_0)->Sig_1:
    if n<=0:
        return Sig_1([s,])
    elif s==[]:
        return  Sig_1([])
    return [s[:n],]+blocks(n,s[n:]) # [take(n,s),]+blocks(n,drop(n,s))
                                    # to make the type checker happy, we can do (its harder to read)
                                    # Sig_1(Sig_1([Sig_0(s[:n]),])+blocks(n,Sig_0(s[n:])))

Sigor=ListFunctor