import qOne.maze as maze


class SearchAlgo(object):

	def __init__(self, maze: maze.Maze):
		self.maze = maze
		self.dim = maze.getDim()
		self.max_fringe = None

	def search(self) -> list:
		pass

	def get_max_fringe(self) -> int:
		return self.max_fringe