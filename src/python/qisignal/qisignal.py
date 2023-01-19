import numpy as np
from collections.abc import Iterable
from more_itertools import chunked
from qiplot import plot_ts
import utils
from interval import interval
import functor

# the case of np=nn
def order_indexes(n,m):
    return np.roll(list(range(n)),m)

# assuming signal on the [0,1]
# padding zero to the left of the origin
def pad_left(sig,pad_size):
    return np.append(sig,np.repeat(0,pad_size))

# assuming signal on the [-1,0]
# padding eor to the right of the origin
def pad_right(sig,pad_size):
    return np.append(np.repeat(0,pad_size),sig)

class signal_i(interval):
    """
    interval signal class
    
    """
    def __init__(self,t,x):
        if not utils.is_sorted(t):
            raise NameError('time stamp not in order')
        nn=utils.nnegatives(t)
        f = len(t)-nn-1
        l = -nn
        interval.__init__(self,x,l,f)
        if isinstance(t,list):
            self.T=np.array(t,dtype=float)
        elif isinstance(t,np.ndarray):
            self.T=t
        else:
            raise TypeError("known type")
        self.T.flags.writeable=False
    
    def plot(self,ax):
        dd = self.ORIGIN
        plot_ts(ax,self.T,dd)

class signal_p(object):
    """
    Periodic signal class

    """
    def __init__(self,t,x):
        if len(t)!=len(x):
            raise ValueError("size of t and x are not the same")
        if not utils.is_sorted(t):
            raise NameError('time stamp not in order')
        nn=utils.nnegatives(t)
        f = len(t)-nn-1
        l = -nn
        self.NN=nn
        self.DATA=np.roll(x,l)
        if isinstance(t,list):
            self.T=np.array(t,dtype=float)
        elif isinstance(t,np.ndarray):
            self.T=t
        else:
            raise TypeError("known type")
        self.DATA.flags.writeable=True
        self.T.flags.writeable=False
    
    def __len__(self):
        return len(self.DATA)

    def __getitem__(self,position):
        return self.DATA[position]

    def __setitem__(self,position,value):
        self.DATA[position]=value

    def plot(self,ax):
        plot_ts(ax,self.T,np.roll(self.DATA,self.NN))

# localization
class blocks(functor.Tuple):
    def __init__(self,sig:tuple,B: int):
        if not isinstance(sig,Iterable) or not isinstance(B,int):
            raise TypeError("sig must be tuple, B must be int")
        functor.Tuple.__init__(self,tuple(tuple(i) for i in chunked(sig,B)))

def decimation(sig):
    return sig[::2]