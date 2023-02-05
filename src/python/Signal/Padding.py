from typing import NewType
from enum import Enum
from Signal.Types import SigNum

Extensions = NewType('Extensions',tuple[list[SigNum],list[SigNum]])
PaddingMethodNames=Enum('PaddingMethod',['ZERO','PERIODIC','SYMETRIC'])

def zero(n:int,v:list[SigNum])->Extensions:
    if n<0 or n>len(v):
        raise ValueError("Illegal Input")
    return Extensions(([0.0 for _ in range(n)],[0.0 for _ in range(n)]))

def periodic(n:int,v:list[SigNum])->Extensions:
    if n<0 or n>len(v):
        raise ValueError("Illegal Input")
    return Extensions((v[-n:],v[:n]))

def symetric(n:int,v:list[SigNum])->Extensions:
    if n<0 or n>len(v):
        raise ValueError("Illegal Input")
    return Extensions((v[:n][::-1],v[-n:][::-1]))

padding={name:method for (name,method) in zip(PaddingMethodNames,(zero,periodic,symetric))}
