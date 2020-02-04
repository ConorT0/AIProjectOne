"""
The Maze class represents a single maze, of size nxn with probability weight p.
0 is a free space, 1 is a blocked space, 2 is a fire
"""
import random


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
		# keep start and goal empty
		self.grid[0][0] = 0
		self.grid[-1][-1] = 0

	# return an array of the 2d grid
	def getGrid(self):
		return self.grid

	# TODO: fill out what this method does
	def updateFire(self):
		pass

	# perform a BFS on the grid
	def bfs(self):
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
		pass

	def printGrid(self):
		for i in self.grid:
			print(*i, sep=" ")
