import AStar
import maze

class AStarManhatten(AStar.AStar):
	def __init__(self, maze):
		super(AStarManhatten, self).__init__(maze)

	def heuristic(self, item:tuple) ->float:
		return abs(item[0] - self.maze.getDim()) + abs(item[1] - self.maze.getDim())

if __name__=='__main__':
	m = maze.Maze(100,.2)
	A = AStarManhatten(m)
	path = A.search()
	m.print_with_temp_path(path)