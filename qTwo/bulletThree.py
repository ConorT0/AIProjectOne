import numpy as np
from matplotlib import pyplot as plt
import qOne.maze as maze
import qOne.dfs as dfs

class findSolveability(object):
	def __init__(self):
		self.dim = 100
		self.step = .03
		self.p = 0
		self.mazePerP = 100
		self.maxP = .6
		i = 0.0
		arr = []
		while i < self.maxP:
			arr.append(i)
			i+= self.step
		self.plotx = np.array(arr)
		self.ploty = []

	def runTest(self):
		self.p = 0
		while self.p < self.maxP: # loop over p values, step up by predefined amount
			solvedMazes = 0
			for x in range(0, self.mazePerP): # make this number of mazes
				m = maze.Maze(self.dim,self.p)
				d = dfs.Dfs(m)
				result = d.search() # run dfs
				if(result is not None): # add one to counter for each solved maze
					solvedMazes += 1
			self.ploty.append(solvedMazes / self.mazePerP) # divide number of solvable mazes by total number of mazes generated.
			self.p += self.step

		self.ploty = np.array(self.ploty)
		print(self.plotx)
		print(self.ploty)
		plt.title("Density VS. Maze solvability for graph of size " + str(self.dim))
		plt.xlabel("Density")
		plt.ylabel("Solvability")
		plt.plot(self.plotx,self.ploty) # plot using pyplot

		plt.show()


f = findSolveability()
f.runTest()