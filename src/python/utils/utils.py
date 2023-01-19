import numpy as np
import collections
from itertools import islice, takewhile, repeat, starmap

def is_even(n: int):
    return (n%2)==0
        
def is_sorted(t):
    return all(a <= b for a, b in zip(t, t[1:]))

# Function to left rotate arr[] of size n by d
# A Juggling Algorithm
# https://www.geeksforgeeks.org/python-program-for-program-for-array-rotation-2/
def left_rotate(arr, d):
    n = len(arr)
    d = d%n
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

# number of negatives in a sorted array
def nnegatives(t):
    nn = 0
    for i in t:
        if i<0:
            nn+=1
        else:
            break
    return nn

def ispower2(n):
    return (n & (n-1) == 0) and n != 0

def generator(iterable,func,*argv):
    return takewhile(bool,map(tuple,starmap(func,
                     repeat((iter(iterable),*argv)))))

def consume(iterator, n=None):
    "Advance the iterator n-steps ahead. If n is None, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)
