import pyglet
from pyglet import clock
from pyglet import shapes
from pyglet.window import mouse
import matchgame
from matchgame import tile
from matchgame import state

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

window = pyglet.window.Window (width=cols*size, height=rows*size+20)

score_label = pyglet.text.Label ('Score: 0',
                                 font_size=16,
				 x  = 10,
				 y = rows*size)



@window.event
def on_draw ():
	window.clear()
	score_label.draw()
	for i in range (rows):
		for j in range (cols):
			grid[i][j].draw()

@window.event
def on_mouse_press (x, y, button, modifiers):
	# which element in the grid
	mx = x // size
	my = y // size

	if (state.num_selected > 0):
		grid[state.selected_x][state.selected_y].click()
		if ((mx == state.selected_x) and (my == state.selected_y)):
			state.num_selected = 0
		else:
			if (mx == state.selected_x):
				if (((my+1) == state.selected_y) or ((my-1) == state.selected_y)):
					grid[mx][my].swap (grid[state.selected_x][state.selected_y])
					state.num_selected = 0
				else:
					grid[mx][my].click()
					state.selected_x = mx
					state.selected_y = my
				check_matches()
				return

			if (my == state.selected_y):
				if (((mx+1) == state.selected_x) or ((mx-1) == state.selected_x)):
					grid[mx][my].swap (grid[state.selected_x][state.selected_y])
					state.num_selected = 0
				else:
					grid[mx][my].click()
					state.selected_x = mx
					state.selected_y = my
				check_matches()
				return

			grid[mx][my].click()
			state.selected_x = mx
			state.selected_y = my
	else:
		grid[mx][my].click()
		state.num_selected = 1
		state.selected_x = mx
		state.selected_y = my
	check_matches()

def refresh_tiles (delta_time):
	for t in state.marked_list:
		t.refresh()

	state.marked_list.clear()

def check_matches ():
	# iterate through grid looking for 8 in a row
	# look for a vertical match
	for i in range (rows):
		for j in range (0, cols-3):
			target_color = grid[i][j].color
			match = 1
			for x in range (1,3):
				if (grid[i][j+x].color != target_color):
					match = 0
			if (match == 1):
				for x in range (3):
					grid[i][j+x].mark ()
					state.marked_list.append (grid[i][j+x])
					state.score = state.score + 1
	
	score_label.text = 'Score: ' + str(state.score)
	clock.schedule_once (refresh_tiles, 5)



pyglet.app.run ()