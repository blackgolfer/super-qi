# https://stackoverflow.com/questions/54162257/a-function-composition-operator-in-python
import functools
import inspect

class Composable:

    def __init__(self, func):
        self._func = func
        functools.update_wrapper(self, func)

    def __getattr__(self, othername):
        stack = inspect.stack()[1][0]
        other = stack.f_locals[othername]
        return Composable(lambda *args, **kw: self._func(other._func(*args, **kw)))

    def __call__(self, *args, **kw):
        return self._func(*args, **kw)