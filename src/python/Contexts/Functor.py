from typing import TypeVar, TypeVarTuple, Generic, Callable

A=TypeVar('A')
As=TypeVarTuple('As')
B=TypeVar('B')
Bs=TypeVarTuple('Bs')

class Functor(Generic[A]):
    pass

class ListFunctor(list[A],Functor[A]):

    def fmap(self,f:Callable[[A],B])->Functor[B]:
        return ListFunctor(map(f,self))
    
class TupleFunctor(tuple[A,...],Functor[A]):

    def fmap(self,f:Callable[[A],B])->Functor[B]:
        return TupleFunctor(map(f,self))