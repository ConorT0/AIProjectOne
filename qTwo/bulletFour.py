import numpy as np
from matplotlib import pyplot as plt
import qOne.maze as maze
import qOne.AStarManhatten as AStarManhatten

class findSolveability(object):
	def __init__(self):
		self.dim = 100
		self.step = .03
		self.p = 0
		self.mazePerP = 1
		self.maxP = .27
		i = 0.0
		arr = []
		while i < self.maxP:
			arr.append(i)
			i+= self.step
		self.plotx = np.array(arr)
		self.ploty = []

	def runTest(self):
		self.p = 0
		while self.p < self.maxP: # loop over p values up to max
			totalPathLength = 0
			x = 0
			while x <self.mazePerP: # generate the right number of graphs per p
				m = maze.Maze(self.dim, self.p)
				a = AStarManhatten.AStarManhatten(m)
				path = a.search()
				if path is not None: # only count path if it is not none.
					totalPathLength += len(path)
					x+=1
			self.ploty.append(totalPathLength / self.mazePerP) # add the average length

			self.p += self.step

		self.ploty = np.array(self.ploty)
		print(self.plotx)
		print(self.ploty)
		plt.title("Density VS. Expected path length for graph of size " + str(self.dim))
		plt.xlabel("Density")
		plt.ylabel("Expected Path Length")
		plt.plot(self.plotx, self.ploty)  # plot using pyplot

		plt.show()

f = findSolveability()
f.runTest()