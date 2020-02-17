from qOne import maze
import random
from qOne import bibfs
import copy
from qOne import AStarEuclid
import numpy as np

class FireMaze(maze.Maze):
	def __init__(self, dim: int, maze_probability: float, fireProbability: float):
		self.fireProbability = fireProbability
		self.fire_path = set()
		# inheritance proofing
		self.path = list()

		self.current_path = list()

		super().__init__(dim, maze_probability)

		# get some path it doesn't matter
		# and make sure it has a solution to a non-fire grid
		self.gen_until_basic_path_exists()

		# ensure start cell has valid path to initial fire cell
		self.gen_fire_start()

		# inheritance proofing
		self.fire_progress = list()
		self.historic_path = list()

	# given a cell, find all the neighbors that are on fire
	def count_on_fire_neighbors(self, cell: tuple) -> int:
		r = cell[0]
		c = cell[1]
		k = 0

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
					if np.random.random() <= cell_probability and self.grid[r][c] != 1:
						cells_caught_on_fire.add((r, c))

		# update the grid with the new cells
		# we have to do this separately
		self.fire_path = self.fire_path.union(cells_caught_on_fire)

	def gen_fire_start(self) -> tuple:
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
				self.reset()
				self.generateGrid()

	def get_fire_path(self) -> set:
		return self.fire_path

	def reset_fire(self):
		self.fire_path = set()
		self.fire_progress = list()

	def reset(self):
		super().clear_grid()
		self.reset_fire()
		self.current_path = list()
		self.historic_path = list()

	def reset_but_keep_same_grid_and_same_fire_start(self):
		self.reset()
		self.grid = copy.deepcopy(self.original_grid)
		self.path = copy.deepcopy(self.original_path)
		self.current_path = self.path
		self.fire_path.add(self.fire_start)

	def gen_until_basic_path_exists(self):
		# get some path it doesn't matter
		# and make sure it has a solution to a non-fire grid
		while True:
			a = AStarEuclid.AStarEuclid(self)
			self.path = a.search()

			if self.path is None:
				self.reset()
				self.generateGrid()
			else:
				self.original_path = copy.deepcopy(self.path)
				break

	def reset_hard(self):
		self.reset()
		self.original_grid = list()
		self.original_path = list()

		self.gen_until_basic_path_exists()

		self.gen_fire_start()
		self.current_path = self.path
		self.original_path = copy.deepcopy(self.current_path)


if __name__ == '__main__':
	test = FireMaze(10, 0.1, 1)
	for x in range(0,100):
		print(test.fire_path)
		test.updateFire()

	print()
	test.printGrid()
