from typing import TypeVar, Generic, Iterable, Protocol, Any
from abc import ABCMeta, abstractmethod

A=TypeVar('A')

class Renderer(Generic[A]):
    @abstractmethod
    def save(self,filename:str,transparent:bool)->None: ...
    @abstractmethod
    def show(self)->None: ...
    @abstractmethod
    def drawables(self)->list[A]: ...
    @abstractmethod
    def graphicStore(self)->Any: ...

class Drawable(Generic[A]):
    pass

class Draw(Protocol):
    def diagram(self,gps:list[Any])->Renderer: ...
    def toDrawable(self,gp:Any)->Drawable: ...
