import qOne.maze as maze
import random
from qOne import bibfs
import copy

class FireMaze(maze.Maze):
	def __init__(self, dim: int, maze_probability: float, fireProbability: float):

		self.FIRE_SYMBOL = 6

		super(FireMaze, self).__init__(dim, maze_probability)
		self.fireProbability = fireProbability
		self.fire_path = set()

		# ensure start cell has valid path to initial fire cell
		self.gen_fire_start()

	# given a cell, find all the neighbors that are on fire
	def count_on_fire_neighbors(self, cell: tuple) -> int:
		r = cell[0]
		c = cell[1]
		k = 0

		grid = self.getGrid()

		if r > 0:
			if (r - 1, c) in self.fire_path:
				k += 1
		if r < self.getDim() - 1:
			if (r + 1, c) in self.fire_path:
				k += 1
		if c > 0:
			if (r, c - 1) in self.fire_path:
				k += 1
		if c < self.getDim() - 1:
			if (r, c + 1) in self.fire_path:
				k += 1

		return k

	# updates the cells that are on fire with the given initial probability
	def updateFire(self) -> None:

		# create a list that will contain all the cells that are now caught on fire
		cells_caught_on_fire = set()
		for r in range(0, len(self.getGrid())):
			for c in range(0, len(self.getGrid()[0])):
				if (r, c) not in self.fire_path:
					k = self.count_on_fire_neighbors((r, c))
					cell_probability = 1 - pow((1 - self.fireProbability), k)
					if random.uniform(0, 1) <= cell_probability and self.grid[r][c] != 1:
						cells_caught_on_fire.add((r, c))

		# update the grid with the new cells
		# we have to do this separately
		self.fire_path = self.fire_path.union(cells_caught_on_fire)

	def gen_fire_start(self):
		# we don't want the first cell, and we don't want the last cell (dim - 1 is the last cell)
		# randomly pick a cell to initially set on fire
		r = random.randint(1, self.dim - 2)
		c = random.randint(1, self.dim - 2)
		# check that (0,0) has a path to (r,c)
		while True:
			p = bibfs.BiDirectionalBFS(self, (0, 0), (r, c)).search()
			if p is not None:
				self.fire_path.add((r, c))
				self.fire_start = (r, c)
				break
			else:
				self.clear_grid()
				self.generateGrid()

	def get_fire_path(self) -> set:
		return self.fire_path

	def reset_fire(self):
		self.fire_path = set()

if __name__ == '__main__':
	test = FireMaze(10, 0.1, 1)
	for x in range(0,100):
		print()
		test.printGrid()
		test.updateFire()

	print()
	test.printGrid()
