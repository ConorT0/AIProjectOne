import collections
import time
import qOne.maze as maze
import qOne.algo as algo

class Dfs(algo.SearchAlgo):
	def __init__(self, maze):
		self.maze = maze
		self.fringe =  collections.deque()
		self.max_fringe = -1
		# make prev array
		self.prev = [[None for j in range(maze.getDim())] for i in range(maze.getDim())]

	def search(self):
		startTime = time.perf_counter ()
		self.fringe.append((0,0))
		self.prev[0][0] = (0,0)
		self.max_fringe = 1
		#use pop() to get item from queue
		while(self.fringe): # This checks if the dequeue is empty? python is such a mystical language...
			item = self.fringe.pop()  # remove
			for i in self.validNeighbors(item): # get all valid neighbors,
				if(self.maze.getGrid()[i[0]][i[1]] == 'g'):#if the neighbor is the goal
					backtrack = i
					next = item
					path = []

					while(next!=backtrack):
						path.append(backtrack)
						#grid[backtrack[0]][backtrack[1]] = '*' # Starting from the goal node, look at the prev. continue until you hit the first node. Mark with stars.
						backtrack = next
						next = self.prev[backtrack[0]][backtrack[1]]

					return path
				else:
					self.fringe.append(i) # add valid neighbor to fringe
					self.prev[i[0]][i[1]] = item # make valid neighbor's prev value the current node.

			self.max_fringe = max(self.max_fringe,len(self.fringe))

		return None



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


class Dfsbad(algo.SearchAlgo):
	def __init__(self, maze):
		self.maze = maze
		self.fringe =  collections.deque()
		# make prev array
		self.prev = [[None for j in range(maze.getDim())] for i in range(maze.getDim())]

	def search(self):
		startTime = time.perf_counter ()
		self.fringe.append((0,0))
		self.prev[0][0] = (0,0)
		self.max_fringe = 1
		#use pop() to get item from queue
		while(self.fringe): # This checks if the dequeue is empty? python is such a mystical language...
			item = self.fringe.pop()  # remove
			for i in self.validNeighbors(item): # get all valid neighbors,
				if(self.maze.getGrid()[i[0]][i[1]] == 'g'):#if the neighbor is the goal
					backtrack = i
					next = item
					path = []

					while(next!=backtrack):
						path.append(backtrack)
						#grid[backtrack[0]][backtrack[1]] = '*' # Starting from the goal node, look at the prev. continue until you hit the first node. Mark with stars.
						backtrack = next
						next = self.prev[backtrack[0]][backtrack[1]]

					return path
				else:
					self.fringe.append(i) # add valid neighbor to fringe
					self.prev[i[0]][i[1]] = item # make valid neighbor's prev value the current node.

			self.max_fringe = max(self.max_fringe,len(self.fringe))

		return None



	def validNeighbors(self, item):

		ret = []
		i = item[0]
		j = item[1]
		grid = self.maze.getGrid()


		# left
		if j - 1 != -1 and (grid[i][j - 1] == 0 or grid[i][j - 1] == 'g') and self.prev[i][j - 1] is None:
			ret.append((i, j - 1))

		# down
		if i + 1 < len(grid) and (grid[i + 1][j] == 0 or grid[i + 1][j] == 'g') and self.prev[i + 1][j] is None:
			ret.append((i + 1, j))

		# to the right. If it is not outside of the maze, is a free spot, and has not been visited yet, we pass this check.
		if j + 1 < len(grid) and (grid[i][j + 1] == 0 or grid[i][j + 1] == 'g') and self.prev[i][j + 1] is None:
			ret.append((i, j+1))

		# item above. If it is not outside of the maze, is a free spot, and has not been visited yet, we pass this check.
		if i - 1 != -1 and (grid[i - 1][j] == 0 or grid[i - 1][j] == 'g') and self.prev[i - 1][j] is None:
			ret.append((i - 1, j))
		return ret



if __name__ == '__main__':

	m = maze.Maze(100,.2)

	d = Dfs(m)
	path = d.search()



	m.print_with_temp_path(path)

