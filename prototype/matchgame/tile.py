import random
import pyglet
from pyglet import shapes

class tile:

	def __init__(self, x, y) -> None:
	    pass

	def draw (self):
		pass

	def click (self):
		pass

	def swap (self, partner):
		pass

	def mark (self):
		pass

class basic (tile):

	colortable = { "red" : (255,0,0),
			"green" : (0,255,0),
			"blue" : (0,0,255)}

	def __init__(self, x, y) -> None:
	    super().__init__(x, y)
	    self.highlight = shapes.Circle (x*20+10, y*20+10, 9, color=(255, 255, 255)) 
	    self.color = random.choice (list (self.colortable.keys()))
	    self.circle = shapes.Circle (x*20+10, y*20+10, 6, color=self.colortable[self.color]) 
	    self.selected = 0

	def draw(self):
	    if (self.selected == 1):
	    	self.highlight.draw()
	    self.circle.draw()
	    return super().draw()

	def click (self):
		self.selected = 1 - self.selected

	def swap (self, partner):
		tmp_color = partner.color
		partner.color = self.color
		self.color = tmp_color

		partner.circle.color = self.colortable[partner.color]
		self.circle.color = self.colortable[self.color]

		partner.circle.draw()
		self.circle.draw()

	def mark (self):
		self.circle.color = (0,0,0)
		self.circle.draw()
