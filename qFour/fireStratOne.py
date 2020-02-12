import maze
import fireMaze
import AStarManhatten


class fireAStar(fireMaze.FireMaze):

	def __init__(self, dim: int, maze_probability: float, fireProbability: float):
		super(fireAStar, self).__init__(dim, maze_probability, fireProbability)
		a = AStarManhatten.AStarManhatten(self.maze)
		self.path = a.search()

	# walk the solved path, and on each step update the cells that are on fire
	# returns a list with how far we were able to get in the path
	# if the entire list is returned that means we were successful
	# TODO: paint how far we got in the maze & the fire
	def walk_fire_maze(self):
		for step in range(0, self.path):
			r = self.path[step][0]
			c = self.path[step][1]

			if self.grid[r][c] == '🔥':
				return self.path[0:step]

			self.updateFire()

		return self.path
