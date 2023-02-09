from typing import NewType
from enum import Enum
from Signal.Types import sig_0

Extensions = NewType('Extensions',tuple[sig_0,sig_0])
PaddingMethodNames=Enum('PaddingMethod',['ZERO','PERIODIC','SYMETRIC'])

def zero(n:int,v:sig_0)->Extensions:
    if n<0 or n>len(v): raise ValueError("Illegal Input")
    else: return Extensions(([0.0]*n,[0.0]*n))

def periodic(n:int,v:sig_0)->Extensions:
    if n<0 or n>len(v): raise ValueError("Illegal Input")
    else: return Extensions((v[-n:],v[:n]))

def symetric(n:int,v:sig_0)->Extensions:
    if n<0 or n>len(v): raise ValueError("Illegal Input")
    else: return Extensions((v[:n][::-1],v[-n:][::-1]))

padding={name:method for (name,method) in zip(PaddingMethodNames,(zero,periodic,symetric))}
