"""
The Maze class represents a single maze, of size nxn with probability weight p.
0 is a free space, 1 is a blocked space, 2 is a fire
"""
import random
import collections
import copy

class Maze(object):

	def __init__(self, dim: int, probability: float):
		self.probability = probability
		self.dim = dim  # size of the graph
		self.grid = [[0 for x in range(dim)] for y in range(dim)] # Make a dim x dim grid
		self.generateGrid()
		self.path = list()

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

	def updateCell(self, data: any, r: int, c: int):
		self.grid[r][c] = data

	def get_grid_int_matrix_with_temp_path(self, path) -> list:
		if path == None or path == []:
			return None
		else:
			grid_copy = copy.deepcopy(self.grid)
			for cell in path:
				grid_copy[cell[0]][cell[1]] = 2

			grid_copy[0][0] = 3
			grid_copy[-1][-1] = 4

			return grid_copy

	def get_grid_with_temp_path(self, path) -> str:
		out = str()
		if path == None or path == []:
			return "\x1b[5;30;41mFailure\x1b[0m"
		else:
			grid_copy = copy.deepcopy(self.grid)
			for cell in path:
				grid_copy[cell[0]][cell[1]] = "\x1b[6;30;42m#\x1b[0m"

			grid_copy[0][0] = 's'
			grid_copy[-1][-1] = 'g'

			for row in grid_copy:
				for cell in row:
					out += " " + str(cell)
				out += "\n"

			return out

	def print_with_temp_path(self, path) -> None:
		print(self.get_grid_with_temp_path(path))

	def printGrid(self) -> None:
		for i in self.grid:
			print(*i, sep=" ")

	def clear_grid(self):
		self.grid = [[0 for x in range(self.dim)] for y in range(self.dim)]

if __name__ == "__main__":
	import maze
	import bibfs
	myM = maze.Maze(100, 0.1)
	doB = bibfs.BiDirectionalBFS(myM)

	myM.print_with_temp_path(doB.search())