from Graphic.AbstractLayers import Draw
from typing import Any

class Display():
	def __init__(self,d:Draw,objs:list[Any])->None:
		self.objs=objs; self.draw=d
	
	def __enter__(self):
		return self.draw.diagram(self.objs)

	def __exit__(self, *args):
		pass
