import numpy as np

#-------------------------------------------------------
# Precomputed rising cutoff function (rcf) for grid
# point and mid point foldings
# 
# Inputs:
# E - number of sampling points on the interval (0,1]
# num - rcf parameter, for sine iteration, this is the
#       number of iteration
#
# Internal variables:
# _grid: store the precomputed rcf for sampled at grid
#        point
#        _grid[i]*_grid[i]+_grid[-i]*_grid[-i]=1
# _mid: store the precomputed rcf for mid point sampled
#       _mid[i]*_mid[i]+_mid[-i-1]*_mid[-i-1]=1
#------------------------------------------------------
class rcf:
    def __init__(self,E,num=1):
        self._E=E
        self._num_itr=num
        self._type='mid'
        self._grid=np.empty(2*self._E-1,dtype=float)
        self._mid=np.empty(2*self._E,dtype=float)
        self.__rcfgrid()
        self.__rcfmid()

    def settype(self,type):
        if type=='grid' or type=='mid':
            self._type=type
        else:
            raise NameError("invalid type")

    def type(self):
        return self._type

    def final(self):
        return self._E-1

    def least(self):
        if self._type == 'grid':
            return -self._E+1
        else:
            return -self._E
        
    def __getitem__(self,position):
        if self._type=='grid':
            return self._grid[position]
        else:
            return self._mid[position]

    def __len__(self):
        if self._type=='grid':
            return len(self._grid)
        else:
            return len(self._mid)

    # for now we just use the iterative sine
    # we will deal with multiple rcf later
    def rcfis(self,t,N=1):
        if t>-1.0:
            if t<1.0:
                for i in range(0,N):
                    t = np.sin(0.5*np.pi*t)
                t = np.sin(0.25*np.pi*(1.0+t))
            else:
                t = 1.0
        else:
            t = 0.0
        return t

    def order_indexes(self):
        if (self._type=='grid'):
            oi = list(range(2*self._E-1))
            return np.roll(oi,self._E-1)
        else:
            oi = list(range(2*self._E))
            return np.roll(oi,self._E)

    def num_itr(self):
        return self._num_itr

    # rcf sampled at grid point
    # declare rcfgrid as private method
    # the array is arranged as:
    #   _grid[1]..._grid[E] for rcf at t=1/E,2/E,...,1
    #   _grid[:-1]..._grid[:-E] for rcf at t=-1/E,-2/E,...,-1
    def __rcfgrid(self):
        t=0.0
        dt=1.0/self._E # 1/(final+1)
        self._grid[0]=np.sqrt(0.5)
        for j in range(1,self._E):
            t=t+dt
            self._grid[j] = self.rcfis(t,self._num_itr)
            self._grid[-j] = self.rcfis(-t,self._num_itr)

    # rcf sampled at mid point
    # declare rcfmid as private method
    # the array is arranged as:
    # _grid[1]..._grid[E]: for rcf at (0+1/2)/E,(1+1/2)/E,...,1-1/(2E)
    # _grid[-1]..._grid[:-E+1]: for rcf at -(0+1/2)/E,-(1+1/2)/E,...,-1+1/(2E)
    def __rcfmid(self):
        t = 0.5/self._E
        dt = 1.0/self._E
        for j in range(0,self._E):
            self._mid[j]=self.rcfis(t,self._num_itr)
            self._mid[-j-1]=self.rcfis(-t,self._num_itr)
            t = t+dt
