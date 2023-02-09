# https://notes.asaleh.net/posts/monoid-pattern-in-python/
from functools import singledispatch, partial

@singledispatch
def mempty(a):
    raise NotImplementedError("Not implemented for " + a)

@singledispatch
def mappend(a, b):
    raise NotImplementedError("Not implemented for " + a)

@singledispatch
def mconcat(a):
    raise NotImplementedError("Not implemented for "+a)

@mempty.register(list)
def _(a): return []

@mappend.register(list)
def _(a,b): return a + b

@mconcat.register(list)
def _(a): return list((x for xs in a for x in xs))

@mconcat.register(tuple)
def _(a): return tuple((x for xs in a for x in xs))

@mempty.register(tuple)
def _(a): return ()

@mappend.register(tuple)
def _(a,b): return a+b

@mempty.register(None.__class__)
def _(a): return None

@mappend.register(None.__class__)
def _(a,b): return None

def func(v:list[list])->list: # just for the function type
    return [x for xs in v for x in xs]

@mappend.register(func.__class__)
def _(a,b):
  def result(*x):
    a_r= a(*x)
    b_r=b(*x)
    return mappend(a_r,b_r)
  return result

@mappend.register(partial)
def _(a,b):
    return [a,b]
