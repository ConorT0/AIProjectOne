import copy

from qOne import bibfs
from qFour import fireMaze
import collections
from qOne import dfs
from qFour import fireStrat

class FireStratTwo():

	def __init__(self, maze: fireMaze.FireMaze):
		self.maze = maze
		self.maze.current_path = self.maze.path
		self.survived_fire = False

	# walk the solved path, and on each step update the cells that are on fire
	# returns a list with how far we were able to get in the path
	# if the entire list is returned that means we were successful
	# TODO: paint how far we got in the maze & the fire
	def walk_fire_maze(self):

		while True:
			# slowly store the path taken
			self.maze.historic_path.append(self.maze.current_path[0])

			# burn the fire one more iteration
			self.maze.updateFire()
			self.maze.fire_progress.append(list(self.maze.fire_path))

			# take a step by searching for a new path from the current cell
			if len(self.maze.current_path) == 1:
				# we made it to goal
				self.survived_fire = True
				break
			else:
				a = FireBiBFS(self.maze, start=self.maze.current_path[1])
				self.maze.current_path = a.search()

			if self.maze.current_path is None:
				break

		return self.maze.historic_path

class FireBiBFS(bibfs.BiDirectionalBFS):
	def __init__(self, maze: fireMaze.FireMaze, start: tuple):
		self.maze = maze
		super(FireBiBFS, self).__init__(self.maze, start=start, single_mode=True)

	def find_valid_adjacent_nodes(self, matrix_node: tuple, visited: set, prev: dict, fringe: collections.deque):

		valid_nodes = collections.deque()

		r = matrix_node[0]
		c = matrix_node[1]

		grid = self.maze.getGrid()

		# check if the adjacent nodes are within the bounds of the grid
		# also check if the adjacent nodes aren't blocked off
		if r > 0:
			n = (r - 1, c)
			if grid[r - 1][c] != 1 and (r - 1, c) not in self.maze.fire_path:
				n not in visited and n not in prev and n not in fringe and valid_nodes.append(n)
		if r < self.maze.getDim() - 1:
			n = (r + 1, c)
			if grid[r + 1][c] != 1 and (r + 1, c) not in self.maze.fire_path:
				n not in visited and n not in prev and n not in fringe and valid_nodes.append(n)
		if c > 0:
			n = (r, c - 1)
			if grid[r][c - 1] != 1 and (r, c - 1) not in self.maze.fire_path:
				n not in visited and n not in prev and n not in fringe and valid_nodes.append(n)
		if c < self.maze.getDim() - 1:
			n = (r, c + 1)
			if grid[r][c + 1] != 1 and (r, c + 1) not in self.maze.fire_path:
				n not in visited and n not in prev and n not in fringe and valid_nodes.append(n)

		return valid_nodes


if __name__ == "__main__":
	f = fireMaze.FireMaze(25, 0.2, 0.2)
	m = FireStratTwo(f)
	p = m.walk_fire_maze()

	g = copy.deepcopy(f.grid)
	g = f.get_grid_int_temp_matrix_with_temp_path(grid=g, path=f.fire_path, data=6)
	g = f.get_grid_int_temp_matrix_with_temp_path(grid=g, path=p, data=2)

	f.gen_and_save_graphs_with_temp_grid_only(grid=g, graph_title="Fire Strategy Two", fname="fstrat2.png", save=False)