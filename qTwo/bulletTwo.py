from qOne import maze
from qOne import bfs
from qOne import dfs
from qOne import AStarEuclid
from qOne import AStarManhatten
from qOne import bibfs
import time
import copy
from matplotlib import colors as c
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

	# 100 because its sufficiently hard enough for BFS
	MAZE_SIZE = 100

	# run each algorithm on the list of mazes, get avg times
	algos_map = {
		"astareuclid": AStarEuclid.AStarEuclid,
		"astarmanhattan": AStarManhatten.AStarManhatten,
		"bfs": bfs.Bfs,
		"bibfs": bibfs.BiDirectionalBFS,
		"dfs": dfs.Dfs
	}

	# run for each maze
	for algo_name, algo in algos_map.items():

		path = None

		while True:

			m = maze.Maze(MAZE_SIZE, 0.2)
			a = algo(m)
			path = a.search()
			if path is not None:

				break

		grid_copy = copy.deepcopy(m.get_grid_int_matrix_with_temp_path(path))

		grid_copy = np.pad(grid_copy, pad_width=1, mode='constant', constant_values=5)
		cMap = c.ListedColormap(['w', 'r', 'y', 'grey', 'green', 'black'])

		plt.pcolormesh(grid_copy, cmap=cMap)

		plt.axes().set_aspect('equal')  # set the x and y axes to the same scale
		plt.xticks([])  # remove the tick marks by setting to an empty list
		plt.yticks([])  # remove the tick marks by setting to an empty list
		plt.axes().invert_yaxis()  # invert the y-axis so the first row of data is at the top

		plt.show()

		plt.clf()
		plt.cla()
		plt.close()







