from qOne import maze
# My approach for making harder mazes will be very simple: instead of definining neighbors as the same node with another
# block added anywhere in random walk, neighbors will be a block added in the path that the algo took.
# All neighbors would be each cell in the path blocked. For example, if the path is of length 10, then there will be
# 10 neighbors, each one with a different cell blocked.
#
from qOne import AStarManhatten
from qOne import dfs
from qOne import maze

class mazeEnhancer(object):
	def __init__(self, maze:maze):
		self.maze = maze
		self.unsolvable = False
		if AStarManhatten(maze).search() is None:
			print("Supplied maze has no solution")
			self.unsolvable = True

	def getNeighbors(self) -> [maze]:
		pass




