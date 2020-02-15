"""
The Maze class represents a single maze, of size nxn with probability weight p.
0 is a free space, 1 is a blocked space, 2 is a fire
"""
import random
import copy
from matplotlib import colors as c
import matplotlib.pyplot as plt
import numpy as np
import os

class Maze(object):

	def __init__(self, dim: int, probability: float):
		self.probability = probability
		self.dim = dim  # size of the graph
		self.grid = [[0 for x in range(dim)] for y in range(dim)] # Make a dim x dim grid
		self.generateGrid()
		self.path = list()
		self.rank = -1 # rank is "hardness" of maze

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

	def get_grid_int_temp_matrix_with_temp_path(self, path: list, grid: list, data: int) -> list:
		grid_copy = copy.deepcopy(grid)

		grid_copy[0][0] = 3
		grid_copy[-1][-1] = 4

		if path is not None and path is not []:
			for cell in path:
				grid_copy[cell[0]][cell[1]] = data

		return grid_copy

	def get_grid_int_matrix_with_temp_path(self, path: list) -> list:

		return self.get_grid_int_temp_matrix_with_temp_path(path, self.grid, 2)

	def get_grid_with_temp_path(self, path: list) -> str:
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



	def gen_and_save_graphs_with_temp_grid_only(self, grid: list, save_path: str = "./", fname: str = "unnamed.png", graph_title: str = "Un-named Graph") -> None:

		grid = np.pad(grid, pad_width=1, mode='constant', constant_values=5)
		cMap = c.ListedColormap(['w', 'r', 'y', 'grey', 'green', 'black', 'orange'])

		plt.pcolormesh(grid, cmap=cMap)

		plt.title(graph_title)

		plt.axes().set_aspect('equal')  # set the x and y axes to the same scale
		plt.xticks([])  # remove the tick marks by setting to an empty list
		plt.yticks([])  # remove the tick marks by setting to an empty list
		plt.axes().invert_yaxis()  # invert the y-axis so the first row of data is at the top

		plt.savefig(os.path.join(save_path, fname), dpi = 300, bbox_inches='tight')

		plt.cla()
		plt.clf()
		plt.close()

	def gen_and_save_graphs_with_temp_path_and_temp_grid(self, path: list, grid: list, save_path: str = "./", fname: str = "unnamed.png", graph_title: str = "Un-named Graph"):
		return self.gen_and_save_graphs_with_temp_grid_only(grid=self.get_grid_int_temp_matrix_with_temp_path(grid = grid, path=path, data=2), save_path=save_path, fname=fname, graph_title=graph_title)

	def gen_and_save_graphs_with_temp_path(self, path: list, save_path: str = "./", fname: str = "unnamed.png", graph_title: str = "Un-named Graph"):
		grid = self.get_grid_int_matrix_with_temp_path(path)
		return self.gen_and_save_graphs_with_temp_path_and_temp_grid(path, grid, save_path, fname, graph_title)

	def print_with_temp_path(self, path) -> None:
		print(self.get_grid_with_temp_path(path))

	def printGrid(self) -> None:
		for i in self.grid:
			print(*i, sep=" ")

	def clear_grid(self):
		self.grid = [[0 for x in range(self.dim)] for y in range(self.dim)]

	def __gt__(self, other):
		if self.rank!=-1 and other.rank !=-1:
			return self.rank > other.rank
	def __ge__(self, other):
		if self.rank!=-1 and other.rank !=-1:
			return self.rank >= other.rank

if __name__ == "__main__":
	import maze
	import bibfs
	myM = maze.Maze(100, 0.1)
	doB = bibfs.BiDirectionalBFS(myM)

	myM.print_with_temp_path(doB.search())