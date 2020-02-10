import maze
import AStar
import random

class FireMaze(maze.Maze):
	def __init__(self, dim: int, probability: float, fireProbability: float):
		super(FireMaze, self).__init__(dim, probability)
		self.fireProbability = fireProbability

		# we don't want the first cell, and we don't want the last cell (dim - 1 is the last cell)
		# randomly pick a cell to initially set on fire
		self.updateCell('🔥', random.randint(1, self.dim - 2), random.randint(1, self.dim - 2))

	def count_on_fire_neighbors(self, cell: tuple) -> int:
		r = cell[0]
		c = cell[1]
		k = 0

		grid = self.getGrid()

		if r > 0:
			if grid[r - 1][c] == '🔥':
				k += 1
		if r < self.maze.getDim() - 1:
			if grid[r + 1][c] == '🔥':
				k += 1
		if c > 0:
			if grid[r][c - 1] == '🔥':
				k += 1
		if c < self.maze.getDim() - 1:
			if grid[r][c + 1] == '🔥':
				k += 1

		return k

	# TODO: fill out what this method does
	def updateFire(self) -> None:
		cells_caught_on_fire = list()
		for r in self.getGrid():
			for c in r:
				k = self.count_on_fire_neighbors((r, c))
				cell_probability = 1 - ((1 - self.fireProbability)**k)
				if (random.uniform(0, 1) <= cell_probability):
					cells_caught_on_fire.append((r, c))

if __name__ == '__main__':
	test = FireMaze(100, 0.1, 0.2)

	test.generateFire()
	test.updateFire()

	test.printGrid()
