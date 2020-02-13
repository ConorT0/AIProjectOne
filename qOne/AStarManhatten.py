import qOne.AStar as AStar
import qOne.AStar as AStar
import qOne.maze as maze

class AStarManhatten(AStar.AStar):
	def __init__(self, maze):
		super(AStarManhatten, self).__init__(maze)

	def heuristic(self, item:tuple) ->float:
		return abs(item[0] - self.maze.getDim()+ 1) + abs(item[1] - self.maze.getDim() +1 ) # return the dis. +1 is off by one error due to 0 indexing of arrays.

if __name__=='__main__':
	m = maze.Maze(100,0)
	A = AStarManhatten(m)
	path = A.search()
	m.print_with_temp_path(path)