from qOne import maze

import random

class FireMaze(maze.Maze):
	def __init__(self, dim: int, probability: float, fireProbability: float):
		super(FireMaze, self).__init__(dim, probability)
		self.fireProbability = fireProbability

		# we don't want the first cell, and we don't want the last cell (dim - 1 is the last cell)
		# randomly pick a cell to initially set on fire
		self.updateCell('🔥', random.randint(1, self.dim - 2), random.randint(1, self.dim - 2))
		#self.updateCell('🔥', 1,1)
	def count_on_fire_neighbors(self, cell: tuple) -> int:
		r = cell[0]
		c = cell[1]
		k = 0

		grid = self.getGrid()

		if r > 0:
			if grid[r - 1][c] == '🔥':
				k += 1
		if r < self.getDim() - 1:
			if grid[r + 1][c] == '🔥':
				k += 1
		if c > 0:
			if grid[r][c - 1] == '🔥':
				k += 1
		if c < self.getDim() - 1:
			if grid[r][c + 1] == '🔥':
				k += 1

		return k

	# TODO: fill out what this method does
	def updateFire(self) -> None:
		cells_caught_on_fire = list()
		for r in range(0,len(self.getGrid())):
			for c in range(0,r):
				k = self.count_on_fire_neighbors((r, c))
				cell_probability = 1 - pow((1 - self.fireProbability),k)
				if (random.uniform(0, 1) <= cell_probability):
					cells_caught_on_fire.append((r, c))
		for cell in cells_caught_on_fire:
			self.updateCell('🔥', cell[0],cell[1])

if __name__ == '__main__':
	test = FireMaze(10, 0.1, 1)
	for x in range(0,100):
		print()
		test.printGrid()
		test.updateFire()

	print()
	test.printGrid()
