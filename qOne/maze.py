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

	def getGrid(self):
		return self.grid

	def updateFire(self):
		print('not done dont look')

	def printGrid(self):
		for i in self.grid:
			print(*i, sep=" ")
