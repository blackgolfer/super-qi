import numpy as np
from lft.rcf import rcf

# $U$ operator
# r must be mid sampled
def fipc(sig,r):
    if r.type()!='mid':
        raise ValueError
    for k in range(r.final()+1):
        # r(t)f(t)+r(-t)f(-t)
        tmp = r[k]*sig[k]+r[-k-1]*sig[-k-1]
        # r(t)f(-t)-r(-t)f(t)
        sig[-k-1]=r[k]*sig[-k-1]-r[-k-1]*sig[k]
        sig[k]=tmp

# $U^*$ operator
# r must be mid sampled
def fips(sig,r):
    if r.type()!='mid':
        raise ValueError
    for k in range(r.final()+1):
        # r(t)f(t)-r(-t)f(-t)
        tmp = r[k]*sig[k]-r[-k-1]*sig[-k-1]
        # r(t)f(-t)+r(-t)f(t)
        sig[-k-1]=r[k]*sig[-k-1]+r[-k-1]*sig[k]
        sig[k]=tmp

uipc=fips
uips=fipc
