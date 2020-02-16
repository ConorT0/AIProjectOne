import copy

from qOne import bibfs
from qFour import fireMaze
import collections

class FireStratTwo(fireMaze.FireMaze):

	def __init__(self, dim: int, maze_probability: float, fireProbability: float):
		super(FireStratTwo, self).__init__(dim, maze_probability, fireProbability)

		# we need to first check and make sure that without the fire, we have a solution in general
		# if we don't generate a new grid
		while True:
			a = bibfs.BiDirectionalBFS(self)
			self.path = a.search()

			if self.path is None:
				self.clear_grid()
				self.generateGrid()
			else:
				break

		self.current_path = self.path
		self.historic_path = list()
		self.fire_progress = list()

	# walk the solved path, and on each step update the cells that are on fire
	# returns a list with how far we were able to get in the path
	# if the entire list is returned that means we were successful
	# TODO: paint how far we got in the maze & the fire
	def walk_fire_maze(self):

		while True:
			# slowly store the path taken
			self.historic_path.append(self.current_path[0])

			# burn the fire one more iteration
			self.updateFire()
			self.fire_progress.append(list(self.fire_path))

			# take a step by searching for a new path from the current cell
			if len(self.current_path) == 1:
				break
			else:
				a = FireBiBFS(self, start=self.current_path[1])
				self.current_path = a.search()

			if self.current_path is None:
				break

		return self.historic_path


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
	f = FireStratTwo(25, 0.2, 0.2)
	p = f.path
	p = f.walk_fire_maze()

	g = copy.deepcopy(f.grid)
	g = f.get_grid_int_temp_matrix_with_temp_path(grid=g, path=f.fire_path, data=6)
	g = f.get_grid_int_temp_matrix_with_temp_path(grid=g, path=p, data=2)

	f.gen_and_save_graphs_with_temp_grid_only(grid=g, graph_title="Fire Strategy Two", fname="fstrat2.png", save=False)