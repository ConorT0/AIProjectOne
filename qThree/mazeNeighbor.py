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
	#do note that the heapq does it backwards for some reason. not the end of the world
	def getMaxNeightbor(self) -> [maze.Maze]:
		topmazes = []
		maxrank = 0
		for i in range(0, self.maze.getDim()):
			for j in range(0, self.maze.getDim()):
				if (i != 0 and j != 0) and (
						i != self.maze.getDim() - 1 and j != self.maze.getDim() - 1):  # dont want to invert first or last.
					self.changedCell = (i, j) # choose the cell to invert
					self.invertCell() # invert it
					rank =0
					if (self.type): # calculate rank
						rank = self.rankDFS()
					else:
						rank = self.rankAstar()
					maxrank = max(maxrank,rank)
					if(len(topmazes) <self.topn): # if we have space just stick it in the heap
						cop = copy.deepcopy(self.maze)
						cop.rank = rank
						heapq.heappush(topmazes,(cop))
					elif rank > topmazes[0].rank: # if we dont have space, only stick it on if it is better than the worst one
						heapq.heappop(topmazes) # delete the easiest maze
						cop = copy.deepcopy(self.maze)
						cop.rank=rank
						heapq.heappush(topmazes, cop) # add the current maze
					self.invertCell()
		print (maxrank)
		return topmazes

	def rankDFS(self) -> int:
		d = dfs.Dfs(self.maze)
		path = d.search()
		if path is None:
			return 0
		return d.get_max_fringe()

	def rankAstar(self) -> int:
		aStar = AStarManhatten.AStarManhatten(self.maze)
		path = aStar.search()
		if path is None:
			return 0
		return aStar.getNodesExplored()

	def invertCell(self):
		cell = self.maze.getGrid()[self.changedCell[0]][self.changedCell[1]]
		if(cell == 0):
			self.maze.getGrid()[self.changedCell[0]][self.changedCell[1]] = 1
		elif (cell == 1):
			self.maze.getGrid()[self.changedCell[0]][self.changedCell[1]] = 0
		else:
			print('encounted invalid cell.')


m = maze.Maze(10,.2)
mnm = mazeNeightborManager(m,True,5)
x = mnm.getMaxNeightbor()
print(x)

