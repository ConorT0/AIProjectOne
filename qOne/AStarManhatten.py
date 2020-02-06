import time
import queue
import qOne.maze
class AStarManhatten(object):
	def __init__(self, maze):
		self.maze = maze
		self.fringe = queue.PriorityQueue()
		self.prev = [[None for j in range(maze.getDim())] for i in range(maze.getDim())]

	def search(self):
		pass

	def heuristic(self):
		pass

	def validNeighbors(self, item):

		ret = []
		i = item[0]
		j = item[1]
		grid = self.maze.getGrid()
		# item above. If it is not outside of the maze, is a free spot, and has not been visited yet, we pass this check.
		if i - 1 != -1 and (grid[i - 1][j] == 0 or grid[i - 1][j] == 'g') and self.prev[i - 1][j] is None:
			ret.append((i - 1, j))

		# left
		if j - 1 != -1 and (grid[i][j - 1] == 0 or grid[i][j - 1] == 'g') and self.prev[i][j - 1] is None:
			ret.append((i, j - 1))

		# down
		if i + 1 < len(grid) and (grid[i + 1][j] == 0 or grid[i + 1][j] == 'g') and self.prev[i + 1][j] is None:
			ret.append((i + 1, j))

		# to the right. If it is not outside of the maze, is a free spot, and has not been visited yet, we pass this check.
		if j + 1 < len(grid) and (grid[i][j + 1] == 0 or grid[i][j + 1] == 'g') and self.prev[i][j + 1] is None:
			ret.append((i, j+1))