from qOne import bibfs
from qOne import AStarManhatten
from qOne import maze


if __name__ == "__main__":
	m = maze.Maze(100, 0.2)
	astar = AStarManhatten.AStarManhatten(m)
	bdbfs = bibfs.BiDirectionalBFS(m)

	astar_path = astar.search()
	bdbfs_path = bdbfs.search()

	m.gen_and_save_graphs_with_temp_path(astar_path, fname="a.png", graph_title="AStar")
	m.gen_and_save_graphs_with_temp_path(bdbfs_path, fname="bd.png", graph_title="BiBFS")