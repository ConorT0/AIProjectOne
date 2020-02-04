"""
The Maze class represents a single maze, of size nxn with probability weight p.
0 is a free space, 1 is a blocked space, 2 is a fire
"""
import random
import collections


class Maze(object):

	def __init__(self, dim: int, probability: float, fireProbability: float= None):
		self.fireProbability = fireProbability
		self.probability = probability
		self.dim = dim  # size of the graph
		self.grid = [[0 for x in range(dim)] for y in range(dim)] # Make a dim x dim grid
		self.generateGrid()

	# create a dim x dim sized grid and fill with spaces based on given probability
	def generateGrid(self) -> None:
		for i in range(0,self.dim):
			for j in range(0,self.dim):
				if(random.uniform(0,1) <= self.probability):
					self.grid[i][j] = 1
				else:
					self.grid[i][j] = 0
		# put special markers for start and goal
		self.grid[0][0] = 's'
		self.grid[-1][-1] = 'g'

	# return an array of the 2d grid
	def getGrid(self):
		return self.grid

	# TODO: fill out what this method does
	def updateFire(self):
		pass

	# perform a BFS on the grid
	def bfs(self, fringe: collections.deque = None, start: dict() = None, goal: dict() = None):
		pass

	# perform a DFS on the grid
	def dfs(self):
		pass

	# perform an A* with h(n) = euclidean distance to goal on the grid
	def astar_euclidean(self):
		pass

	# perform an A* with h(n) = manhattan distance to goal on the grid
	def astar_manhattan(self):
		pass

	# perform a bi-directional BFS on the grid
	def bidirectional_bfs(self):
		front = dict(x=0, y=0)
		back = dict(x=self.dim-1, y=self.dim-1)
		visited = set(front, back)
		front_queue = collections.deque(front)
		back_queue = collections.deque(back)

		while front_queue and back_queue:
			if front_queue:
				x = front_queue.popleft()
				if x == back or x in back_queue:
					return True




		pass

	def printGrid(self):
		for i in self.grid:
			print(*i, sep=" ")
