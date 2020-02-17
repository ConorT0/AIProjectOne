import copy
from qFour import fireMaze
from qOne import bibfs
from qOne import dfs
from qOne import AStarEuclid
from qFour import fireStrat


class FireStratOne(fireStrat.FireStrat):

	def __init__(self, maze: fireMaze.FireMaze):
		self.maze = maze
		self.survived_fire = False


	# walk the solved path, and on each step update the cells that are on fire
	# returns a list with how far we were able to get in the path
	# if the entire list is returned that means we were successful
	# TODO: paint how far we got in the maze & the fire
	def walk_fire_maze(self):

		for step in range(0, len(self.maze.path)):
			r = self.maze.path[step][0]
			c = self.maze.path[step][1]

			if (r, c) in self.maze.fire_path:
				return self.maze.path[0:step]
			else:
				# burn the fire more
				self.maze.updateFire()
		# got here so survived:

		self.survived_fire = True
		return self.maze.path


if __name__ == "__main__":
	m = fireMaze.FireMaze(100, 0.2, 0)
	f = FireStratOne(m)

	while False:

		p = f.walk_fire_maze()
		if p == []:
			break
		m.clear_grid()
		m.generateGrid()

	p = f.walk_fire_maze()

	g = copy.deepcopy(f.maze.grid)
	g = m.get_grid_int_temp_matrix_with_temp_path(grid=g, path=m.fire_path, data=6)
	g = m.get_grid_int_temp_matrix_with_temp_path(grid=g, path=p, data=2)

	m.gen_and_save_graphs_with_temp_grid_only(grid=g, graph_title="Fire Strategy One", save=False)
