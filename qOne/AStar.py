import time
import queue
import math
import qOne.maze as maze


class AStar(object):
	def __init__(self, maze):
		self.maze = maze
		self.fringe = queue.PriorityQueue()
		# add items to fringe of pattern (priority_number, data)
		self.prev = [[None for j in range(maze.getDim())] for i in range(maze.getDim())]
		self.prev[0][0] = (0,0)

	def search(self):
		startTime = time.perf_counter()
		goalComplete = False
		maxFringe = 0
		self.fringe.put(self.makeOrderedPair((0,0))) # start off the fringe
		while not goalComplete and not self.fringe.empty():
			item = self.fringe.get()[1]
			if(item[0] == self.maze.getDim()-1 and item[1] == self.maze.getDim()-1):
				goalComplete = True
			else:
				neighbors = self.validNeighbors(item)
				for n in neighbors:
					self.fringe.put(self.makeOrderedPair(n)) # add to fringe, will calculate distance.
					self.prev[n[0]][n[1]] = item # update prev of the new thing in the fringe to be the calling node.
				maxFringe = max(maxFringe, self.fringe.qsize())

		if(goalComplete): # we found the goal
			#grid = [row[:] for row in self.maze.getGrid()]
			#for ite in range(0, self.maze.getDim()):
			#	for itj in range(0, self.maze.getDim()):
			#		if (self.prev[ite][itj] is not None):
			#			grid[ite][itj] = 'f'  # If any cell has a prev, that means it was on the fringe at some point. Mark the cell with an 'f'
			backtrack = (len(self.maze.getGrid())-1, len(self.maze.getGrid())-1)
			next = self.prev[backtrack[0]][backtrack[1]]
			path = []
			while (next != backtrack):
				path.append(backtrack)
				#grid[backtrack[0]][backtrack[
				#	1]] = '*'  # Starting from the goal node, look at the prev. continue until you hit the first node. Mark with stars.
				backtrack = next
				next = self.prev[backtrack[0]][backtrack[1]]
			#grid[-1][-1] = 'g'
			#grid[0][0] = 's'
			print("Found Solution:")
			#self.maze.updatePath(path)
			#self.maze.printGrid()
			#for i in grid:
			#	print(*i, sep=" ")
			print("Max fringe size: " + str(maxFringe))
			print("Took " + str((time.perf_counter() - startTime)) + " seconds")
			return path
		else:
			print('Could not find path using a* for maze:')
			self.maze.printGrid()


	# im lazy
	def makeOrderedPair(self, item):
		return (self.heuristic(item), item)

	# returns the result of the heuristic. Implemented in subclass
	def heuristic(self, item:tuple) ->float:
		pass

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


