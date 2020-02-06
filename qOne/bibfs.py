# perform a bi-directional BFS on the grid
from collections import deque as queue
import maze


class BiDirectionalBFS:

	def __init__(self, m: maze.Maze):
		self.maze = m

		front = (0, 0)
		# back is the goal
		back = (self.maze.getDim() - 1, self.maze.getDim() - 1)

		# define all of the front
		self.front_visited = set()
		self.front_previous = dict()
		self.front_fringe = queue()
		self.front_fringe.append(front)

		# define all of the back
		self.back_visited = set()
		self.back_previous = dict()
		self.back_fringe = queue()
		self.back_fringe.append(back)

	def search(self) -> str:
		while self.front_fringe and self.back_fringe:
			# current front, back
			f, b = self.front_fringe.popleft(), self.back_fringe.popleft()

			# if the current front node that was taken off the front_fringe
			# has already been visited by the back path
			# then the front crossed the a path the back already explored
			if f in self.back_visited:
				# back bfs already crossed this path
				return self.generate_path_from(f)

			else:
				# if the current front node has not been visited by the back yet
				# then get all the valid adjacent nodes
				valid_nodes = self.find_valid_adjacent_nodes(f, self.front_visited)
				# add them to the fringe
				self.front_fringe += valid_nodes
				# then associate them with f in the previous dict
				for n in valid_nodes:
					self.front_previous[n] = f

				self.front_visited.add(f)

			# if the current front node that was taken off the front_fringe
			# has already been visited by the back path
			# then the front crossed the a path the back already explored
			if b in self.front_visited:
				# front bfs already crossed this path
				return self.generate_path_from(b)
			else:
				# if the current front node has not been visited by the back yet
				# then get all the valid adjacent nodes
				valid_nodes = self.find_valid_adjacent_nodes(b, self.back_visited)
				# add them to the fringe
				self.back_fringe += valid_nodes
				# then associate them with f in the previous dict
				for n in valid_nodes:
					self.back_previous[n] = b

				self.back_visited.add(b)

		return "failure"

	def find_valid_adjacent_nodes(self, matrix_node: tuple, visited: set):

		valid_nodes = queue()

		r = matrix_node[0]
		c = matrix_node[1]

		grid = self.maze.getGrid()

		# check if the adjacent nodes are within the bounds of the grid
		# also check if the adjacent nodes aren't blocked off
		if r > 0:
			n = (r - 1, c)
			if grid[r - 1][c] != 1:
				n not in visited and valid_nodes.append(n)
		if r < self.maze.getDim() - 1:
			n = (r + 1, c)
			if grid[r + 1][c] != 1:
				n not in visited and valid_nodes.append(n)
		if c > 0:
			n = (r, c - 1)
			if grid[r][c - 1] != 1:
				n not in visited and valid_nodes.append(n)
		if c < self.maze.getDim() - 1:
			n = (r, c + 1)
			if grid[r][c + 1] != 1:
				n not in visited and valid_nodes.append(n)

		return valid_nodes

	def generate_path_from(self, node: tuple):
		# connect the two paths at the middle
		f,b = node, node
		f_path, b_path = [], []
		m = self.maze.getGrid()
		while True:
			f_path.append(f)
			if m[f[0]][f[1]] == 's':
				break
			f = self.front_previous[f]


		while True:
			b_path.append(b)
			if m[b[0]][b[1]] == 'g':
				break
			b = self.back_previous[b]

		f_path.reverse()
		# start b_path from 1 instead of 0 since they both contain same node
		# we could also do f_path[:-1]
		res = f_path + b_path[1:]
		return res


if __name__ == "__main__":

	myM = maze.Maze(10, 0.1)
	doB = BiDirectionalBFS(myM)
	myM.printGrid()
	print(doB.search())












