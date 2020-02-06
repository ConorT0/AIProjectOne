import time
import queue
import math
import maze


class AStarEuclid(object):
	def __init__(self, maze):
		self.maze = maze
		self.fringe = queue.PriorityQueue()
		# add items to fringe of pattern (priority_number, data)
		self.prev = [[None for j in range(maze.getDim())] for i in range(maze.getDim())]

	def search(self):
		pass

	def heuristic(self, item:tuple) ->float:
		return math.sqrt((item[0]-self.maze.getDim())**2 + (item[1]-self.maze.getDim())**2)

	# reused from dfs
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

if __name__=='__main__':
	A = AStarEuclid(qOne.maze.Maze(10,.2))
	print(A.heuristic((10,10)))
	#TODO heurisitic needs to account for arrays being 0 indexed? i think.