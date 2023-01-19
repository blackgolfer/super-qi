from typing import Generic, TypeVar, Callable
from immutable import Immutable

A = TypeVar("A")
B = TypeVar("B")

class Maybe(Generic[A]):
    pass

class Just(Maybe[A],Immutable):

    def __init__(self, val: A):
        self.val = val

    def fmap(self, func: Callable[[A], B]) -> Maybe[B]:
        try:
            new_val = func(self.val)
            return Just(new_val)
        except Exception as e:
            return Nothing()

    def bind(self, func: Callable[[A], Maybe[B]]) -> Maybe[B]:
        try:
            new_val = func(self.val)
            return new_val
        except Exception as e:
            return Nothing()

class Nothing(Maybe[A]):

    def fmap(self, func: Callable[[A], B]) -> Maybe[B]:
        return self
    
    def bind(self, func: Callable[[A], Maybe[B]]) -> Maybe[B]:
        return self