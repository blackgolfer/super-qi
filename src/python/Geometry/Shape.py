from __future__ import annotations
from dataclasses import dataclass, field
from nptyping import NDArray, Float, Int
import nptyping
from typing import NewType
import numpy as np
from Contexts.Foldable import foldl

P2=NewType('P2',NDArray[nptyping.Shape["2, 1"], Float])

def point2(p:tuple[float,float])->P2:
    return P2(np.matrix([[p[0]],[p[1]]]))

def polar2(r:float,theta:float)->P2:
    return point2((r*np.cos(theta),r*np.sin(theta)))
    
def unp2(p:P2)->tuple[float,float]:
    return (float(p[0]),float(p[1]))

def unpolar2(p:P2)->tuple[float,float]:
    x,y=unp2(p)
    return (np.linalg.norm(p),np.arctan2(x,y))

def midpoint(e1:P2,e2:P2):
    return P2(0.5*(e1+e2))

class Shape():
    pass

@dataclass
class Line2(Shape): # two dimensional straight line
    e1:P2
    e2:P2

    def length(self)->np.float64:
        return np.linalg.norm(self.e2-self.e1)
    def __repr__(self) -> str:
        return str((self.e1,self.e2))
    
@dataclass
class Circle2(Shape):
    radius:float
    center:P2=field(default_factory=lambda:point2((0,0)))

def vertices2lines(vs:list[P2])->list[Line2]:
    return foldl(lambda acc,x:acc+[Line2(acc[-1].e2,x),],[Line2(vs[0],vs[1]),],vs[2:]+[vs[0]])
def boundary2vertices(lines:list[Line2])->list[P2]:
    return foldl(lambda acc,x:acc+[x.e1,x.e2],[],lines)[:-1]

@dataclass
class Polygon2(Shape):
    boundary:list[Line2]

    @classmethod
    def PolygonRegular(cls,center:P2,radius:float,n:int)->Polygon2:
        if n<3: raise ValueError("Illegal number of sides")
        ps=[polar2(radius/np.cos(np.pi/n),2*x*np.pi/n) for x in range(n)]
        return cls(vertices2lines(ps))
    @classmethod
    def Triangle(cls,es:list[Line2])->Polygon2:
        if len(es)!=3: raise ValueError("Illegal input for triangle")
        else: return cls(es)
    @classmethod
    def Rectangle(cls,es:list[Line2])->Polygon2:
        if len(es)!=4: raise ValueError("Illegal input for rectangle")
        else: return cls(es)
    @classmethod
    def Pentagon(cls,es:list[Line2])->Polygon2:
        if len(es)!=5: raise ValueError("Illegal input for pentagon")
        else: return cls(es)

def ps2matrix(ps): return foldl(lambda acc,x: np.append(acc,x,axis=1),ps[0],ps[1:])
def l2matrix(line): return np.append(line.e1,line.e2,axis=1)
def lines2matrix(ls): return foldl(lambda acc,x: np.append(acc,l2matrix(x),axis=1),l2matrix(ls[0]),ls)
