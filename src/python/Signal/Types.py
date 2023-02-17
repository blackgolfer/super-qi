import numpy.typing as npt

signum=int|float|complex|str|None|tuple[()]
sig_0=list[signum]|npt.NDArray
sig_1=list[sig_0]
sig_3=list[tuple[sig_0,sig_0,sig_0]]

#from typing import NewType, Union

#SigNum=Union[int,float,complex,str,None,tuple[()]]
#Sig_0 = NewType('Sig_0',list[SigNum])
#Sig_1 = NewType('Sig_1',list[Sig_0])
#Sig_3 = NewType('Sig_3',list[tuple[Sig_0,Sig_0,Sig_0]])
