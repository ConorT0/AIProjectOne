# perform a bi-directional BFS on the grid
from collections import deque as queue
import qOne.maze as maze


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

	def search(self) -> str or list:
		while self.front_fringe and self.back_fringe:

			# do front and back DFS one branch at a time
			f = self.bi_dry_helper(self.front_fringe, self.front_visited, self.back_visited, self.back_previous, self.front_previous)
			b = self.bi_dry_helper(self.back_fringe, self.back_visited, self.front_visited, self.front_previous, self.back_previous)

			if f is not None:
				return self.generate_path_from(f)
			elif b is not None:
				return self.generate_path_from(b)

		return None

	def bi_dry_helper(self, fringe: queue, visited: set, opp_visited: set, opp_prev: dict, prev: dict) -> list or None:
		c = fringe.popleft()

		# if the current front node that was taken off the fringe
		# has already been visited by the opposite path
		# then this crossed the a path the opp already explored
		if c in opp_visited or c in opp_prev:
			# opp bfs already crossed this path
			return c

		else:
			# mark curr node as visited
			visited.add(c)
			# if the current node has not been visited by the opp yet
			# then get all the valid adjacent nodes
			adjacent_nodes = self.find_valid_adjacent_nodes(c, visited, prev, fringe)
			# add them to the fringe
			# then associate them with f in the previous dict
			for n in adjacent_nodes:
				if n not in visited:
					fringe.append(n)
					prev[n] = c

		return None

	def find_valid_adjacent_nodes(self, matrix_node: tuple, visited: set, prev: dict, fringe: queue):

		valid_nodes = queue()

		r = matrix_node[0]
		c = matrix_node[1]

		grid = self.maze.getGrid()

		# check if the adjacent nodes are within the bounds of the grid
		# also check if the adjacent nodes aren't blocked off
		if r > 0:
			n = (r - 1, c)
			if grid[r - 1][c] != 1:
				n not in visited and n not in prev and n not in fringe and valid_nodes.append(n)
		if r < self.maze.getDim() - 1:
			n = (r + 1, c)
			if grid[r + 1][c] != 1:
				n not in visited and n not in prev and n not in fringe and valid_nodes.append(n)
		if c > 0:
			n = (r, c - 1)
			if grid[r][c - 1] != 1:
				n not in visited and n not in prev and n not in fringe and valid_nodes.append(n)
		if c < self.maze.getDim() - 1:
			n = (r, c + 1)
			if grid[r][c + 1] != 1:
				n not in visited and n not in prev and n not in fringe and valid_nodes.append(n)

		return valid_nodes

	def generate_path_from(self, node: tuple):
		# connect the two paths at the middle
		f, b = node, node
		f_path, b_path = [], []
		m = self.maze.getGrid()

		while True:
			f_path.append(f)

			if f == (0, 0):
				break

			f = self.front_previous[f]


		while True:
			b_path.append(b)
			if b == (self.maze.getDim() - 1, self.maze.getDim() - 1):
				break

			b = self.back_previous[b]

		f_path.reverse()
		# start b_path from 1 instead of 0 since they both contain same node
		# we could also do f_path[:-1]
		res = f_path + b_path[1:]

		return res


if __name__ == "__main__":

	myM = maze.Maze(100, 0.1)
	doB = BiDirectionalBFS(myM)

	myM.print_with_temp_path(doB.search())












