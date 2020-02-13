import time
import queue
import math
import qOne.maze as maze
import qOne.algo as algo


class AStar(algo.SearchAlgo):
	def __init__(self, maze):
		self.maze = maze
		self.fringe = queue.PriorityQueue()
		self.maxFringe = -1
		self.nodesExplored = -1
		# add items to fringe of pattern (priority_number, data)
		self.prev = [[None for j in range(maze.getDim())] for i in range(maze.getDim())]
		self.prev[0][0] = (0,0)

	def search(self):
		startTime = time.perf_counter()
		goalComplete = False
		self.maxFringe = 0
		self.nodesExplored = 0
		self.fringe.put(self.makeOrderedPair((0,0))) # start off the fringe
		while not goalComplete and not self.fringe.empty():
			item = self.fringe.get()[1]
			self.nodesExplored +=1
			if(item[0] == self.maze.getDim()-1 and item[1] == self.maze.getDim()-1):
				goalComplete = True
			else:
				neighbors = self.validNeighbors(item)
				for n in neighbors:
					self.fringe.put(self.makeOrderedPair(n)) # add to fringe, will calculate distance.
					self.prev[n[0]][n[1]] = item # update prev of the new thing in the fringe to be the calling node.
				self.maxFringe = max(self.maxFringe, self.fringe.qsize())

		if(goalComplete): # we found the goal
			backtrack = (len(self.maze.getGrid())-1, len(self.maze.getGrid())-1)
			next = self.prev[backtrack[0]][backtrack[1]]
			path = []
			while (next != backtrack):
				path.append(backtrack)
				backtrack = next
				next = self.prev[backtrack[0]][backtrack[1]]

			path.reverse()
			return path



	# im lazy
	def makeOrderedPair(self, item):
		return (self.heuristic(item), item)

	# returns the result of the heuristic. Implemented in subclass
	def heuristic(self, item:tuple) ->float:
		pass

	def getMaxFringe(self):
		return self.maxFringe

	def getNodesExplored(self):
		return self.nodesExplored

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
		return ret

