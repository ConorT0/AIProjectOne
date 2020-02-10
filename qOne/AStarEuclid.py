import AStar
import math
import maze

class AStarEuclid(AStar.AStar):
	def __init__(self, maze):
		super(AStarEuclid,self).__init__(maze)
	def heuristic(self, item:tuple) ->float:
		return math.sqrt((item[0] - self.maze.getDim()) ** 2 + (item[1] - self.maze.getDim()) ** 2)

if __name__=='__main__':
	A = AStarEuclid(maze.Maze(10,.3))
	A.search()