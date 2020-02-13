import qOne.maze as maze


class SearchAlgo(object):

	def __init__(self, maze: maze.Maze, goal: tuple = None, start: tuple = (0,0)):
		self.maze = maze
		self.dim = maze.getDim()
		self.max_fringe = None
		self.goal = (self.dim - 1, self.dim - 1)
		self.start = start

	def search(self) -> list:
		pass

	def get_max_fringe(self) -> int:
		return self.max_fringe