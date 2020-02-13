from qOne import maze
from qOne import dfs
from qOne import AStarManhatten
import copy
import heapq

# This class acts as a wrapper for a maze object, and looks at all neighbors and ranks them.
class mazeNeightborManager(object):
	def __init__(self, maze: maze.Maze, type: bool, topn: int):
		self.maze = maze
		self.randomChance = 0
		self.topn = topn  # keep track of the top n mazes
		self.type = type  # True for DFS false for ASTAR
		self.changedCell = (0, 1)

	def getMaxNeightbor(self) -> maze.Maze:
		topmazes = []
		for i in range(0, self.maze.getDim()):
			for j in range(0, self.maze.getDim()):
				if (i != 0 and j != 0) and (
						i != self.maze.getDim() - 1 and j != self.maze.getDim() - 1):  # dont want to invert first or last.
					self.changedCell = (i, j)
					self.invertCell()
					rank =0
					if (self.type):
						rank = self.getMaxNeighborDFS()
					else:
						rank = self.getMaxNeightborManhatten()
					if rank > topmazes[0][0]:
						heapq.heappop(topmazes) # delete the easiest maze
						heapq.heappush(topmazes, (rank, copy.deepcopy(self.maze))) # add the current maze
					self.invertCell()
		return topmazes

	def rankDFS(self) -> int:
		d = dfs.Dfs(self.maze)
		path = d.search()
		return d.get_max_fringe()

	def rankAstar(self) -> int:
		aStar = AStarManhatten.AStarManhatten(self.maze)
		path = aStar.search()
		return aStar.getNodesExplored()

	def invertCell(self):
		cell = self.maze.getGrid()[self.changedCell[0]][self.changedCell[1]]
		if(cell == 0):
			self.maze.getGrid()[self.changedCell[0]][self.changedCell[1]] = 1
		elif (cell == 1):
			self.maze.getGrid()[self.changedCell[0]][self.changedCell[1]] = 0
		else:
			print('encounted invalid cell.')

