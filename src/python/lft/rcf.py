from abc import ABCMeta, abstractmethod
import numpy as np

class rcf(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,E,type):
        self._E=E
        if type=='grid' or type=='mid':
            self._type=type
        else:
            raise ValueError
        if self._type=='grid':
            self._data=np.empty(2*self._E-1,dtype=float)
            self.__rcfgrid()
        else:
            self._data=np.empty(2*self._E,dtype=float)
            self.__rcfmid()

    def __getitem__(self,position):
        return self._data[position]

    def __len__(self):
        return len(self._data)

    @abstractmethod
    def rcf_fct(self,t):
        pass

    @abstractmethod
    def param(self):
        pass

 
    def __rcfgrid(self):
        """
        rcf sampled at grid point
        the array is arranged as:
            _grid[1]..._grid[E] for rcf at t=1/E,2/E,...,1
            _grid[:-1]..._grid[:-E] for rcf at t=-1/E,-2/E,...,-1
        """
        t=0.0
        dt=1.0/self._E # 1/(final+1)
        self._data[0]=np.sqrt(0.5)
        for j in range(1,self._E):
            t=t+dt
            self._data[j] = self.rcf_fct(t)
            self._data[-j] = self.rcf_fct(-t)

    def __rcfmid(self):
        """
        rcf sampled at mid point

        the array is arranged as:
            _grid[1]..._grid[E]: for rcf at (0+1/2)/E,(1+1/2)/E,...,1-1/(2E)
            _grid[-1]..._grid[:-E+1]: for rcf at -(0+1/2)/E,-(1+1/2)/E,...,-1+1/(2E)
        """
        t = 0.5/self._E
        dt = 1.0/self._E
        for j in range(0,self._E):
            self._data[j]=self.rcf_fct(t)
            self._data[-j-1]=self.rcf_fct(-t)
            t = t+dt

    def order_indexes(self):
        if (self._type=='grid'):
            oi = list(range(2*self._E-1))
            return np.roll(oi,self._E-1)
        else:
            oi = list(range(2*self._E))
            return np.roll(oi,self._E)

    def final(self):
        return self._E-1

    def least(self):
        if self._type == 'grid':
            return -self._E+1
        else:
            return -self._E

    def type(self):
        return self._type

class rcfis(rcf):
    def __init__(self,E,type,ni=1):
        self._num_itr=ni
        rcf.__init__(self,E,type)

    @classmethod
    def grid(cls,E,ni=1):
        return cls(E,'grid',ni)

    @classmethod
    def mid(cls,E,ni=1):
        return cls(E,'mid',ni)

    def rcf_fct(self,t):
        if t>-1.0:
            if t<1.0:
                for i in range(0,self._num_itr):
                    t = np.sin(0.5*np.pi*t)
                t = np.sin(0.25*np.pi*(1.0+t))
            else:
                t = 1.0
        else:
            t = 0.0
        return t

    def param(self):
        return self._num_itr

class rcfth(rcf):
    pass