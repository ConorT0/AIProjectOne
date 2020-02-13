import numpy as np
from matplotlib import pyplot as plt
import qOne.maze as maze
import qOne.dfs as dfs

class findSolveability(object):
	def __init__(self):
		self.dim = 100
		self.step = .05
		self.p = 0
		self.mazePerP = 30
		self.maxP = .5
		i = 0.0
		arr = []
		while i < self.maxP:
			arr.append(i)
			i+= self.step
		self.plotx = np.array(arr)
		self.ploty = []

	def runTest(self):
		self.p = 0
		while self.p < self.maxP:
			solvedMazes = 0
			for x in range(0, self.mazePerP):
				m = maze.Maze(self.dim,self.p)
				d = dfs.Dfs(m)
				result = d.search()
				if(result is not None):
					solvedMazes += 1
			self.ploty.append(solvedMazes / self.mazePerP)
			self.p += self.step

		self.ploty = np.array(self.ploty)
		print(self.plotx)
		print(self.ploty)
		plt.title("p value VS. Maze solvability")
		plt.xlabel("p value")
		plt.ylabel("solvability")
		plt.plot(self.plotx,self.ploty)
		plt.show()


f = findSolveability()
f.runTest()