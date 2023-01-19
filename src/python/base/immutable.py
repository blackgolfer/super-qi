import inspect

class Immutable(object):
    """Inherit this class to make the child class immutable"""
    def __setattr__(self, *args):
        if inspect.stack()[1][3] == '__init__':
            object.__setattr__(self, *args)
        else:
            raise TypeError('Cannot modify Immutable instance')

    __delattr__=__setattr__