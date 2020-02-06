import time
import queue
import qOne.maze
class AStarManhatten(object):
	def __init__(self, maze):
		self.maze = maze
		self.fringe = queue.PriorityQueue()
		self.prev = [[None for j in range(maze.getDim())] for i in range(maze.getDim())]