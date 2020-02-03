"""
The Maze class represents a single maze, of size nxn with probability weight p.

"""


class Maze(object):
	def __init__(self, dim: int, probability: float, fireProbability: float= None):
		self.fireProbability = fireProbability
		self.probability = probability
		self.dim = dim
		self.grid = ([0] * dim) * dim  # Make a dim x dim grid

	def generateGrid(self) -> None:
		print('todo dont look')