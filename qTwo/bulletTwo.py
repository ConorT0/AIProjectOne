from qOne import maze
from qOne import bfs
from qOne import dfs
from qOne import AStarEuclid
from qOne import AStarManhatten
from qOne import bibfs

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
	m = maze.Maze(MAZE_SIZE, 0.2)

	for algo_name, algo in algos_map.items():

		a = algo(m)
		path = a.search()

		while True:
			if path is not None:
				break
			else:
				m.clear_grid()
				m.generateGrid()
				path = a.search()

		m.gen_and_save_graphs_with_temp_path(path, "bulletTwo", algo_name + ".png", algo_name)







