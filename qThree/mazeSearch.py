from qOne import maze
# My approach for making harder mazes will be very simple: instead of definining neighbors as the same node with another
# block added anywhere in random walk, neighbors will be a block added in the path that the algo took.
# All neighbors would be each cell in the path blocked. For example, if the path is of length 10, then there will be
# 10 neighbors, each one with a different cell blocked.
#
import heapq
from qThree import mazeNeighbor
from qOne import maze
from qOne import dfs
from qOne import AStarManhatten


class mazeEnhancer(object):
	def __init__(self, noMazes: int, dim: int):
		self.imnumber=0
		self.type = True  # true for bfs, false for ASTAR
		self.mazes = []
		self.noMazes = noMazes
		x = 0
		while (x < noMazes):
			m = maze.Maze(dim, .1)
			if self.type:
				if self.rankDFS(m) != 0:
					self.mazes.append(m)
					x += 1
			else:
				if self.rankAstar(m) != 0:
					self.mazes.append(m)
					x += 1
		self.running = True
		heapq.heapify(self.mazes)

	def rankDFS(self, m:maze.Maze) -> int:
		d = dfs.Dfs(m)
		path = d.search()
		if path is None:
			return 0
		m.gen_and_save_graphs_with_temp_path(path,fname=str(self.imnumber))
		self.imnumber+=1
		m.rank = d.get_max_fringe()
		return d.get_max_fringe()

	def rankAstar(self, m:maze.Maze) -> int:
		aStar = AStarManhatten.AStarManhatten(m)
		path = aStar.search()
		if path is None:
			return 0
		m.gen_and_save_graphs_with_temp_path(path)
		m.rank = aStar.getNodesExplored()
		return aStar.getNodesExplored()

	def explore(self):
		i = 0

		while i<100:
			maxn = []
			for maze in self.mazes:
				topNeighbors = mazeNeighbor.mazeNeightborManager(maze, self.type, self.noMazes)
				maxn.append(topNeighbors.getMaxNeightbor())
			for item in maxn:
				if item[-1] >= self.mazes[0]:  # if the best neighbor is better than the worst current maze
					heapq.heappop(self.mazes)
					heapq.heappush(self.mazes, item[-1])
			i+=1
		for m in self.mazes:
			if(self.type):
				self.rankDFS(m)
			else:
				self.rankAstar(m)

m = mazeEnhancer(2,10)
m.explore()