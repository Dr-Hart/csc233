import pyglet
from pyglet import shapes

class tile:

	def __init__(self, x, y) -> None:
	    pass

	def draw (self):
		pass

	def click (self):
		pass

class basic (tile):

	def __init__(self, x, y) -> None:
	    super().__init__(x, y)
	    self.highlight = shapes.Circle (x*20+10, y*20+10, 8, color=(0, 255, 255)) 
	    self.circle = shapes.Circle (x*20+10, y*20+10, 7, color=(255, 0, 0)) 
	    self.selected = 0

	def draw(self):
	    if (self.selected == 1):
	    	self.highlight.draw()
	    self.circle.draw()
	    return super().draw()

	def click (self):
		self.selected = 1 - self.selected