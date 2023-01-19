import unittest
import numpy as np

from interval import interval

td_list=list(range(-10,54))
td_arr=np.array(td_list,dtype=float)
least=-10
final=10
ilist=interval(td_list,least,final)
iarr=interval(td_arr,least,final)

def isequal(a,b):
    for i in range(len(a)):
        assert(a[i]==b[i])

class TestInterval(unittest.TestCase):

    def test_param(self):
        assert(len(ilist)==(ilist.FINAL-ilist.LEAST+1))

    def test_origin(self):
        assert(ilist[0]==td_list[ilist.ZERO])
        assert(iarr[0]==td_arr[iarr.ZERO])

    def test_index(self):
        assert(ilist[ilist.LEAST]==td_list[0])
        assert(iarr[iarr.LEAST]==td_arr[0])

    def test_slice(self):
        isequal(ilist[:5],td_list[0:(5+ilist.ZERO)])
        isequal(ilist[-5:0],td_list[(ilist.ZERO-5):ilist.ZERO])
        a = iarr[0:5]
        b = td_arr[iarr.ZERO:(5+iarr.ZERO)]
        isequal(a,b)
        a = iarr[-5:0]
        b = td_arr[iarr.ZERO-5:iarr.ZERO]
        isequal(a,b)

    def test_immutability(self):
        try:
            iarr.FINAL+=1
            assert(False)
        except:
            assert(True)

if __name__=='__main__':
    unittest.main()
