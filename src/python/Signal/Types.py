
from typing import NewType

SigNum=int|float|complex|str|None
Sig_0 = NewType('Sig_0',list[SigNum])
Sig_1 = NewType('Sig_1',list[Sig_0])
Sig_3 = NewType('Sig_3',list[tuple[Sig_0,Sig_0,Sig_0]])
