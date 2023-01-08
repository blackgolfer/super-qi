import numpy as np
import qiplot

def left_rotate(arr, d):
    n=len(arr)
    for i in range(np.gcd(d,n)):
         
        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

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

class signal:
    def __init__(self,t,x,type='mid'):
        if type == 'mid' or type=='grid':
            self._type=type
        else:
            raise NameError('invalid type')
        is_sorted = all(a <= b for a, b in zip(t, t[1:]))
        if not is_sorted:
            raise NameError('time stamp not in order')
        self._nn=0
        for i in t:
            if i<0:
                self._nn+=1
            else:
                break
        if self._type=='mid':
            self._np= len(t)-self._nn # number of positive t sampled points
        else:
            self._np= len(t)-self._nn-1
        self._x=np.append(x[self._nn:len(x)],x[0:self._nn])
        self._t=t

    def __len__(self):
        return len(self._x)

    def __getitem__(self,n):
        return self._x[n]

    def __setitem__(self,index,value):
        self._x[index]=value
    
    def shift(self,n):
        left_rotate(self._x,n)

    def order_index(self):
        if self._type=='mid':
            return list(range(self._np,self._np+self._nn))+list(range(0,self._np))
        else:
            return list(range(self._np+1,self._np+self._nn+1))+list(range(0,self._np+1))

    def x(self):
        return self._x
    
    def t(self):
        return self._t

    def plot(self,ax):
        qiplot.plot_ts(ax,self._t,self._x[self.order_index()])

