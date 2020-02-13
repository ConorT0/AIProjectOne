from qOne import maze
from qOne import bfs
from qOne import dfs
from qOne import AStarEuclid
from qOne import AStarManhatten
from qOne import bibfs
import time

import numpy as np

if __name__ == "__main__":

	# m = maze.Maze(10, 0)
	# A = AStarEuclid.AStarEuclid(m)
	# path = A.search()
	# m.print_with_temp_path(path)

	# 100 because its sufficiently hard enough for BFS
	MAZE_SIZE = 10
	TIMES_TO_RUN_INNER_LOOP = 10

	# range of p_values
	p_values = range(1, 8, 1)

	# generate a maze for each p_val
	mazes = list()
	for p in p_values:
		cur_p = p / 20 # steps of .05, .1, .15, ..., .4
		cur_m = maze.Maze(MAZE_SIZE, cur_p)
		cur_m.generateGrid()
		mazes.append(cur_m)

	# run each algorithm on the list of mazes, get avg times

	time_algo_map = dict(
		astareuclid=dict(algo=AStarEuclid.AStarEuclid, times=list()),
		astarmanhattan=dict(algo=AStarManhatten.AStarManhatten, times=list()),
		bfs=dict(algo=bfs.Bfs, times=list()),
		bibfs=dict(algo=bibfs.BiDirectionalBFS, times=list()),
		dfs=dict(algo=dfs.Dfs, times=list())
	)

	# run for each maze
	for cur_maze in mazes:

		# get times for each algorithm on each maze
		for cur_time_algo in time_algo_map:

			# temp list of times that will be averaged
			times_to_avg = list()

			# run this specific algorithm for a number of times
			for j in range(1, TIMES_TO_RUN_INNER_LOOP):

				while True:

					cur_algo = time_algo_map[cur_time_algo]['algo'](cur_maze)

					tic = time.process_time_ns()
					path = cur_algo.search()
					toc = time.process_time_ns()

					# print(tic, toc, path, algo, m.probability, i, j)

					# solution found:
					if path is not None:

						# record time
						times_to_avg.append(toc-tic)
						# end while loop
						break

			time_algo_map[cur_time_algo]['times'].append(np.average(times_to_avg))

		print(time_algo_map)



