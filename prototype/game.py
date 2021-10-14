import pyglet
from pyglet import shapes
from pyglet.window import mouse
import matchgame
from matchgame import tile
from matchgame import util

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

	if (util.num_selected > 0):
		grid[util.selected_x][util.selected_y].click()
		if ((mx == util.selected_x) and (my == util.selected_y)):
			util.num_selected = 0
		else:
			if (mx == util.selected_x):
				if (((my+1) == util.selected_y) or ((my-1) == util.selected_y)):
					grid[mx][my].swap (grid[util.selected_x][util.selected_y])
					util.num_selected = 0
				else:
					grid[mx][my].click()
					util.selected_x = mx
					util.selected_y = my
				check_matches()
				return

			if (my == util.selected_y):
				if (((mx+1) == util.selected_x) or ((mx-1) == util.selected_x)):
					grid[mx][my].swap (grid[util.selected_x][util.selected_y])
					util.num_selected = 0
				else:
					grid[mx][my].click()
					util.selected_x = mx
					util.selected_y = my
				check_matches()
				return

			grid[mx][my].click()
			util.selected_x = mx
			util.selected_y = my
	else:
		grid[mx][my].click()
		util.num_selected = 1
		util.selected_x = mx
		util.selected_y = my
	check_matches()

def check_matches ():
	# iterate through grid looking for 8 in a row
	# look for a vertical match
	for i in range (rows):
		for j in range (0, cols-8):
			target_color = grid[i][j].color
			match = 1
			for x in range (1,8):
				if (grid[i][j+x].color != target_color):
					match = 0
			if (match == 1):
				for x in range (8):
					grid[i][j+x].mark ()
	



pyglet.app.run ()