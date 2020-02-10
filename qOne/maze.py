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
	def getGrid(self) -> list:
		return self.grid

	# return dimension of the maze
	def getDim(self) -> int:
		return self.dim

	# TODO: fill out what this method does
	def updateFire(self):
		pass

	def updateCell(self, data: any, r: int, c: int):
		self.grid[r][c] = data

	def printGrid(self):
		for i in self.grid:
			print(*i, sep=" ")
