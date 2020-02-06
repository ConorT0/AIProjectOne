import maze
from AStar import AStarEuclid
from AStarManhatten import AStarManhatten
from dfs import Dfs
from bibfs import BiDirectionalBFS
from bfs import Bfs

if __name__ == "__main__":
	m = maze.Maze(20, 0.2)

	m.printGrid()

