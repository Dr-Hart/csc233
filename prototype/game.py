import pyglet
from pyglet import shapes
from pyglet.window import mouse
import matchgame
from matchgame import tile

# python practice
# inheritance
# work in progress

size = 20
rows = 20
cols = 20

grid = []
for i in range (rows):
	grid.append ([])
	for j in range (cols):
		grid[i].append( tile.basic (i, j) )

window = pyglet.window.Window (width=cols*size, height=rows*size)



@window.event
def on_draw ():
	window.clear()
	for i in range (rows):
		for j in range (cols):
			grid[i][j].draw()

@window.event
def on_mouse_press (x, y, button, modifiers):
	# which element in the grid
	mx = x // size
	my = y // size
	grid[mx][my].click()

pyglet.app.run ()