import copy
from qOne import AStar
from qFour import fireStratTwo
import math
import queue
from qFour import fireMaze
from qFour import fireStrat

# using AStar because we want to get the
def get_euclidean_distance(a: tuple, b: tuple) -> float:
	return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))

class FireStratThree(AStar.AStar):
	def __init__(self, maze: fireMaze.FireMaze, start: tuple = (0, 0), goal: tuple = None):
		self.start = start
		if goal:
			self.goal = goal
		else:
			self.goal = (maze.getDim() - 1, maze.getDim() - 1)
		self.maze = maze
		self.fringe = queue.PriorityQueue()
		self.prev = dict()
		self.survived_fire = False


	def search(self):
		# add items to fringe of pattern (priority_number, data)

		self.fringe.put(self.makeOrderedPair(self.start))  # start off the fringe
		while not self.fringe.empty():
			item = self.fringe.get()[1]

			if item == self.goal:
				self.survived_fire = True
				break
			else:
				self.maze.updateFire()
				neighbors = self.validNeighbors(item)
				for n in neighbors:
					self.fringe.put(self.makeOrderedPair(n))  # add to fringe, will calculate distance.
					self.prev[n] = item  # update prev of the new thing in the fringe to be the calling node.

		return self.generate_path_from(item)

	def generate_path_from(self, item: tuple) -> list:
		# connect the two paths at the middle
		c = item
		path = list()

		while True:
			path.append(c)

			if c == self.start:
				break

			c = self.prev[c]

		path.reverse()

		return path

	def validNeighbors(self, matrix_node: tuple):

		valid_nodes = set()

		r = matrix_node[0]
		c = matrix_node[1]

		grid = self.maze.getGrid()

		# check if the adjacent nodes are within the bounds of the grid
		# also check if the adjacent nodes aren't blocked off
		if r > 0:
			n = (r - 1, c)
			if grid[r - 1][c] != 1 and (r - 1, c) not in self.maze.fire_path:
				n not in self.prev and valid_nodes.add(n)
		if r < self.maze.getDim() - 1:
			n = (r + 1, c)
			if grid[r + 1][c] != 1 and (r + 1, c) not in self.maze.fire_path:
				n not in self.prev and valid_nodes.add(n)
		if c > 0:
			n = (r, c - 1)
			if grid[r][c - 1] != 1 and (r, c - 1) not in self.maze.fire_path:
				n not in self.prev and valid_nodes.add(n)
		if c < self.maze.getDim() - 1:
			n = (r, c + 1)
			if grid[r][c + 1] != 1 and (r, c + 1) not in self.maze.fire_path:
				n not in self.prev and valid_nodes.add(n)

		return valid_nodes

	def get_distance_of_nearest_fire_block(self, cell: tuple) -> float:
		distances_from_fire = list()

		for fire_cell in self.maze.fire_path:
			# get the distance from the current cell to each node currently on fire
			distances_from_fire.append(get_euclidean_distance(cell, fire_cell))

		# return the closest distance
		return min(distances_from_fire)

	def heuristic(self, item: tuple) -> float:
		# we want to maximize the distance to the nearest block on fire
		# we want to minimize the distance to the goal
		# so we minimize(-1*(distance_to_fire) + distance_to_goal)
		# we do this because the priorityqueue is ordered by smallest
		f_dist = -1 * self.get_distance_of_nearest_fire_block(item)
		g_dist = get_euclidean_distance(item, (self.maze.getDim() - 1, self.maze.getDim() - 1))

		return f_dist + g_dist

	def makeOrderedPair(self, item: tuple) -> tuple:
		return tuple((self.heuristic(item), item))

	def walk_fire_maze(self):
		return self.search()


if __name__ == "__main__":
	f = fireMaze.FireMaze(dim=100, fireProbability=0.2, maze_probability=0.2)
	m = FireStratThree(f)
	p = m.walk_fire_maze()

	g = copy.deepcopy(f.grid)
	g = f.get_grid_int_temp_matrix_with_temp_path(grid=g, path=list(f.fire_path), data=6)
	g = f.get_grid_int_temp_matrix_with_temp_path(grid=g, path=p, data=2)

	f.gen_and_save_graphs_with_temp_grid_only(grid=g, graph_title="Fire Strategy Three w/ q = 0.2", fname="fstrat3.png", save=True)
