from IPython.display import display # only implemented the ipython rendering for now
from Graphic.AbstractLayers import Renderer, Drawable, Draw
from matplotlib import figure, axes, style, rcParams, cm, patches, path, lines, artist, pyplot
from abc import ABCMeta, abstractmethod
from typing import Type
from cycler import cycler
from Geometry.Shape import *
#import Geometry
#style.use(['ggplot','Geometry.presentation'])
#style.use("dark_background")

class DrawableMPL(Drawable[artist.Artist]):
    @abstractmethod
    def __init__(self,s:Shape)->None: ...
    @abstractmethod
    def add_artist(self,ax:axes.Axes)->artist.Artist: ...
    @abstractmethod
    def content(self)->artist.Artist: ...

class RendererMPL(Renderer[DrawableMPL]):
    def __init__(self,ax:axes.Axes,fig:figure.Figure,ds:list[DrawableMPL])->None:
        self.ax=ax;  self.fig=fig; self.ds=ds
    def save(self,filename:str,transparent:bool=False)->None:
        self.fig.savefig(filename,transparent=transparent)
    def show(self)->None:
        #self.fig.show()
        display(self.fig) # using the IPtyhon.display module to render the drawings.
                          # how to handle other media is still an open problem
    def drawables(self)->list[DrawableMPL]: return self.ds
    def graphicStore(self)->axes.Axes: return self.ax

def mplstyle()->None:
    rcParams['mathtext.fontset'] = 'cm'
    rcParams['font.family'] = 'serif'
    rcParams['axes.prop_cycle']=cycler(color=[cm.get_cmap('Greys')(1-i/64) for i in range(64)])
    #rcParams['image.cmap']='Greys'
    rcParams['figure.autolayout'] = True
    rcParams['axes.facecolor'] = 'none'
    rcParams['figure.facecolor'] = 'none'

def setgrid(ax:axes.Axes,fig:figure.Figure,bg:str)->None:
    ax.grid(which='both')
    ax.grid(zorder=0)
    ax.grid(which='major', color='white', linestyle='-',alpha=.5)
    ax.grid(which='minor', color='white', linestyle='-',alpha=0.25)
    ax.tick_params(axis='both', which='major', labelsize=6)
    ax.minorticks_on()
    ax.set_facecolor(bg)
    fig.set_facecolor(bg)

def p2Line2D(e1:P2,e2:P2)->lines.Line2D:
    return lines.Line2D([e1[0],e2[0]],[e1[1],e2[1]])

class Line2MPL(DrawableMPL):
    def __init__(self,l:Line2)->None:
        e1=unp2(l.e1); e2=unp2(l.e2)
        self.line=lines.Line2D([e1[0],e2[0]],[e1[1],e2[1]])
    def add_artist(self,ax:axes.Axes)->artist.Artist:
        return ax.add_line(self.line)
    def content(self)->artist.Artist: return self.line

class Circle2MPL(DrawableMPL):
    def __init__(self,cir:Circle2)->None:
        self.circle=patches.Circle(xy=(cir.center[0],cir.center[1]),radius=cir.radius,fill=False)
    def add_artist(self,ax:axes.Axes)->artist.Artist:
        return ax.add_patch(self.circle)
    def content(self) -> artist.Artist:
        return self.circle

class Polygon2MPL(DrawableMPL):
    def __init__(self,p:Polygon2)->None:
        ps=boundary2vertices(p.boundary)
        self.polygon=patches.Polygon(xy=ps2matrix(ps).transpose().tolist(),fill=False)
    def add_artist(self,ax:axes.Axes)->artist.Artist:
        return ax.add_patch(self.polygon)
    def content(self) -> artist.Artist:
        return self.polygon

class DrawMPL(): # implementing the Draw interface
    shape2drawable:dict[Type[Shape],Type[DrawableMPL]]={}
    shapes=[Line2,Circle2,Polygon2]
    drawables=[Line2MPL,Circle2MPL,Polygon2MPL]
    def __init__(self,size:tuple[float,float]=(4,4),bg:str='None')->None:
        self.figsize=size; self.bgcolor=bg
        #self.fig = pyplot.figure(figsize=self.figsize)
        self.fig = figure.Figure(figsize=self.figsize)
        self.ax  = self.fig.add_subplot(1,1,1)
        self.ax.axis('off')
        self.shape2drawable={s:d for s,d in zip(self.shapes,self.drawables)}
        mplstyle()
        self.renderer=RendererMPL
    def diagram(self,gps:list[Shape])->RendererMPL:
        ps = list(map(lambda x: self.toDrawable(x),gps))
        l=list(map(lambda x: x.add_artist(self.ax),ps)) # delegate the job to drawable objects to add themself to ax
        return self.renderer(self.ax,self.fig,ps)
    def toDrawable(self,gp:Shape)->DrawableMPL:
        if gp.__class__ in self.shape2drawable: return self.shape2drawable[gp.__class__](gp)
        else: raise TypeError("Unkonw geometrical primitive")
    @staticmethod
    def register(s,d)->None: # binding a Shape with a DrawableMPL
        DrawMPL.shape2drawable[s]=d
