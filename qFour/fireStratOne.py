import copy

import maze
import fireMaze
import bibfs


class FireStratOne(fireMaze.FireMaze):

	def __init__(self, dim: int, maze_probability: float, fireProbability: float):
		super().__init__(dim, maze_probability, fireProbability)

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

		self.fire_progress = list()

	# walk the solved path, and on each step update the cells that are on fire
	# returns a list with how far we were able to get in the path
	# if the entire list is returned that means we were successful
	# TODO: paint how far we got in the maze & the fire
	def walk_fire_maze(self):

		for step in range(0, len(self.path)):
			r = self.path[step][0]
			c = self.path[step][1]

			if (r, c) in self.fire_path:
				return self.path[0:step]
			else:
				self.fire_progress.append(list(self.fire_path))
				# burn the fire more
				self.updateFire()

		return self.path

	def sumn(self):


		import matplotlib.animation as animation
		import matplotlib.pyplot as plt
		import copy
		import numpy as np
		from matplotlib import colors as c
		from matplotlib.animation import FuncAnimation

		try:
			plt.style.use('ggplot')
		except:
			pass

		self.updateCell(0, 0, 0)
		self.updateCell(self.dim-1, 0, 0)

		grid = self.get_grid_int_matrix_with_temp_path([])
		grid = np.pad(grid, pad_width=1, mode='constant', constant_values=5)
		cMap = c.ListedColormap(['w', 'r', 'y', 'grey', 'green', 'black', 'orange'])

		fig, ax = plt.subplots(figsize=(self.dim+1, self.dim+1))
		quad = ax.pcolormesh(grid, cmap=cMap)

		plt.axes().set_aspect('equal')  # set the x and y axes to the same scale
		plt.xticks([])  # remove the tick marks by setting to an empty list
		plt.yticks([])  # remove the tick marks by setting to an empty list
		plt.axes().invert_yaxis()  # invert the y-axis so the first row of data is at the top

		def animate(it):
			quad.set_array(np.asmatrix(self.get_grid_int_matrix_with_temp_path(self.fire_progress[it])).flatten())

		anim = FuncAnimation(fig, animate, frames=len(self.fire_progress)-1, repeat=True)
		# fig.show()
		# plt.show()

		mywriter = animation.ImageMagickWriter()

		anim.save("test", writer=mywriter)
		# plt.cla()
		# plt.clf()
		# plt.close()

if __name__ == "__main__":
	f = FireStratOne(10, 0.2, 0.1)

	while False:

		p = f.walk_fire_maze()
		if p == []:
			break
		f.clear_grid()
		f.generateGrid()

	p = f.walk_fire_maze()

	g = copy.deepcopy(f.grid)
	g = f.get_grid_int_temp_matrix_with_temp_path(grid=g, path=f.fire_path, data=6)
	g = f.get_grid_int_temp_matrix_with_temp_path(grid=g, path=p, data=2)

	f.gen_and_save_graphs_with_temp_grid_only(grid=g, graph_title="Fire Strategy One", save=False)
