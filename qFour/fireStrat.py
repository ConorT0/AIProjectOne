from qFour import fireMaze


class FireStrat():
	def __init__(self, maze: fireMaze.FireMaze):
		self.survived_fire = None

	def reset(self):
		self.survived_fire = False