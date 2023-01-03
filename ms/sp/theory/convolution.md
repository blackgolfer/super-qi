# 卷积
We suppose that the signal to be filtered is of the type: $f = {f [0], . . . , f [N − 1]}$, and that the impulse response, it, is can be defined for negative indices, but is, in all cases, of finite size $P$. We must:
    
1. add enough zeros to the two vectors so that they reach the size of $N + P − 1$.
2. move the negative index entries g to the end of the vector (this is customary for cyclic convolutions). 
3. calculate the convolution cyclic by FFT then inverse FFT.
4. extract the indices that interest us from the result and put them back in order (if we want to retrieve the entries with negative indices).
