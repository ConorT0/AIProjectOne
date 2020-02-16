import copy
from qOne import AStar
from qFour import fireStratTwo
import math
import queue
from collections import deque
import fireMaze


# using AStar because we want to get the
def get_euclidean_distance(a: tuple, b: tuple) -> float:
	return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))


class FireStratThree(fireStratTwo.FireStratTwo):

	def __init__(self, dim: int, maze_probability: float, fireProbability: float):
		super(FireStratThree, self).__init__(dim, maze_probability, fireProbability)

	# walk the solved path, and on each step update the cells that are on fire
	# returns a list with how far we were able to get in the path
	# if the entire list is returned that means we were successful
	def walk_fire_maze(self):

		while True:
			# store the next step in the path taken
			self.historic_path.append(self.current_path[0])

			# burn the fire one more iteration
			self.updateFire()
			self.fire_progress.append(list(self.fire_path))

			# take a step by searching for a new path from the current cell
			# if there is only 1 item in the current_path we're done
			if len(self.current_path) == 1:
				break
			else:
				# take the next step and recalculate the path
				# this time using AStar with our custom heuristic
				a = FireAStar(self, start=self.current_path[1])
				self.current_path = a.search()

			# no path found to goal
			if self.current_path is None:
				break

		return self.historic_path

class FireAStar(AStar.AStar):
	def __init__(self, maze: FireStratThree, start: tuple = (0, 0), goal: tuple = None):
		self.start = start
		if goal:
			self.goal = goal
		else:
			self.goal = (maze.getDim() - 1, maze.getDim() - 1)
		self.maze = maze
		self.fringe = queue.PriorityQueue()
		self.prev = dict()

	def search(self):
		# add items to fringe of pattern (priority_number, data)
		self.fringe.put(self.makeOrderedPair(self.start))  # start off the fringe
		while not self.fringe.empty():
			item = self.fringe.get()[1]

			if item == self.goal:
				return self.generate_path()
			else:
				neighbors = self.validNeighbors(item)
				for n in neighbors:
					self.fringe.put(self.makeOrderedPair(n))  # add to fringe, will calculate distance.
					self.prev[n] = item  # update prev of the new thing in the fringe to be the calling node.
		return None

	def generate_path(self):
		# connect the two paths at the middle
		c = self.goal
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
		return (self.heuristic(item), item)


if __name__ == "__main__":
	f = FireStratThree(25, 0.2, 0.2)
	p = f.path
	p = f.walk_fire_maze()

	g = copy.deepcopy(f.grid)
	g = f.get_grid_int_temp_matrix_with_temp_path(grid=g, path=f.fire_path, data=6)
	g = f.get_grid_int_temp_matrix_with_temp_path(grid=g, path=p, data=2)

	f.gen_and_save_graphs_with_temp_grid_only(grid=g, graph_title="Fire Strategy Three", fname="fstrat3.png",
	                                          save=True)
