import copy

from qOne import bibfs
from qFour import fireMaze
from qFour.fireStratTwo import FireBiBFS
import collections

class FireStratThree(fireMaze.FireMaze):

	def __init__(self, dim: int, maze_probability: float, fireProbability: float):
		super(FireStratThree, self).__init__(dim, maze_probability, fireProbability)


		# get some path it doesn't matter
		# and make sure it has a solution to a non-fire grid
		while True:
			a = bibfs.BiDirectionalBFS(self)
			self.path = a.search()

			if self.path is None:
				self.clear_grid()
				self.generateGrid()
			else:
				break

		self.current_path = self.path
		self.historic_path = list()

		self.fire_progress = list()

	# walk the solved path, and on each step update the cells that are on fire
	# returns a list with how far we were able to get in the path
	# if the entire list is returned that means we were successful
	# TODO: paint how far we got in the maze & the fire
	def walk_fire_maze(self):

		while True:
			# slowly store the path taken
			self.historic_path.append(self.current_path[0])

			# burn the fire one more iteration
			self.updateFire()
			self.fire_progress.append(list(self.fire_path))

			# take a step by searching for a new path from the current cell
			if len(self.current_path) == 1:
				break
			else:
				a = FireBiBFS(self, start=self.current_path[1])
				self.current_path = a.search()

			if self.current_path is None:
				break

		return self.historic_path


if __name__ == "__main__":
	f = FireStratThree(25, 0.2, 0.2)
	p = f.path
	p = f.walk_fire_maze()

	g = copy.deepcopy(f.grid)
	g = f.get_grid_int_temp_matrix_with_temp_path(grid=g, path=f.fire_path, data=6)
	g = f.get_grid_int_temp_matrix_with_temp_path(grid=g, path=p, data=2)

	f.gen_and_save_graphs_with_temp_grid_only(grid=g, graph_title="Fire Strategy Three", fname="fstrat3.png")