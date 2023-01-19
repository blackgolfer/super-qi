import numpy as np
#from immutable import Immutable

class interval(object):
    """
    interval class
        this class is designed for data on the time interval [least,final]
        least must be non-positive integer, presenting the number of negative time
        axis points; final must be a non-negative integer, presenting the number of
        positive time axis points.

    Attributes:
    -----------
    least: the number of negative time index
    final: the number of position time index
    zero: the index for zero time index, equals to -least
    origin: the time series sampled data

    methods:
    --------
    """
    def __init__(self,data,least,final):
        """
        Inputs:
        data: data to be copy to origin, data[0]=orgin[least+zero]
        least: the `least` attribute
        final: the `final` attribute
        """
        if not isinstance(least,int) or not isinstance(final,int):
            raise ValueError("Invalid type input in intervel constructor")
        if  least>0 or least>final:
            raise ValueError("Invalid least parameter")
        length=1+final-least
        if length>0 or data is None:
                if len(data)<length:
                    raise ValueError("Invalid input in interval constructor for data")
                self.ORIGIN=np.array(data[0:length],dtype=float)
                self.ORIGIN.flags.writeable=False
        else:
            self.ORIGIIN=None
        self.LEAST=least
        self.FINAL=final
        self.ZERO=-least

    def __len__(self):
        return len(self.ORIGIN)
            
    def __getitem__(self,n):
        if isinstance(n,int):
            if not self.ininterval(n):
                raise ValueError("interval getitem out of bound")
            else:
                return self.ORIGIN[n+self.ZERO]
        elif isinstance(n,slice):
            if n.start==None:
                start=self.LEAST
            else:
                start=n.start
            if n.stop==None:
                stop=self.FINAL
            else:
                stop=n.stop
            if n.step==None:
                step = 1
            else:
                step = n.step
            if self.ininterval(start) and self.ininterval(stop):
                start += self.ZERO
                stop += self.ZERO
                return np.array([self.ORIGIN[i] for i in range(start,stop,step)],dtype=float)
            else:
                raise ValueError("out of bound")
        else:
            raise TypeError("type unkown")

    def ininterval(self,offset):
        if not isinstance(offset,int):
            raise ValueError('invalid input')
        if offset>=self.LEAST and offset<=self.FINAL:
            return True
        else:
            return False
