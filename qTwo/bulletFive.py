#conor is doing this
# this is currently broken. I am going to fix tomorrow.
import numpy as np
from matplotlib import pyplot as plt
import qOne.maze as maze
import qOne.AStarManhatten as AStarManhatten
import qOne.AStarEuclid as AStarEuclid

class compareAStar(object):
	def __init__(self):
		self.p = .2
		self.dim = 100
		self.noMazes = 5
		self.manhattenData=[0,0,0] # 0- average max fringe size, 1- average nodes explored, 2- average path length
		self.euclidData=[0,0,0]

	def runTest(self):
		i =0
		while i < self.noMazes:
			m = maze.Maze(self.dim,self.p)
			man = AStarManhatten.AStarManhatten(m)
			resman = man.search()
			if(resman is not None):
				self.manhattenData[0] = self.manhattenData[0] + man.getMaxFringe()
				self.manhattenData[1] = self.manhattenData[1] + man.getNodesExplored()
				self.manhattenData[2] = self.manhattenData[2] + len(resman) # add data from the last run

				euclid = AStarEuclid.AStarEuclid(m)
				reseuclid = euclid.search()
				self.euclidData[0] = self.euclidData[0] + euclid.getMaxFringe()
				self.euclidData[1] = self.euclidData[1] + euclid.getNodesExplored()
				self.euclidData[2] = self.euclidData[2] + len(reseuclid) # add data from the last run
				i+=1
		self.manhattenData = np.array(self.manhattenData)
		self.euclidData = np.array(self.euclidData)
		divide = lambda x : x/self.noMazes
		vectorDivide = np.vectorize(divide)
		vectorDivide(self.manhattenData)
		vectorDivide(self.euclidData) # divide all elements in both arrays

		# Most of this bar chart code comes from here:
		#https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
		# it is not related to AI so I just reuse.

		ind = np.arange(len(self.manhattenData))  # the x locations for the groups
		width = 0.35  # the width of the bars

		fig, ax = plt.subplots()
		rects1 = ax.bar(ind - width / 2, self.manhattenData, width,
						label='Manhatten')
		rects2 = ax.bar(ind + width / 2, self.euclidData, width,
						label='Euclid')

		# Add some text for labels, title and custom x-axis tick labels, etc.
		ax.set_ylabel('Resource usage')
		ax.set_title('Manhatten vs Euclid')
		ax.set_xticks(ind)
		ax.set_xticklabels(('average max fringe size', 'average nodes explored', 'average path length found'))
		ax.legend()

		self.autolabel(ax, rects1, "left")
		self.autolabel(ax, rects2, "right")

		fig.tight_layout()

		plt.show()

	def autolabel(self, ax, rects, xpos='center'):
		"""
		Attach a text label above each bar in *rects*, displaying its height.

		*xpos* indicates which side to place the text w.r.t. the center of
		the bar. It can be one of the following {'center', 'right', 'left'}.
		"""

		ha = {'center': 'center', 'right': 'left', 'left': 'right'}
		offset = {'center': 0, 'right': 1, 'left': -1}

		for rect in rects:
			height = rect.get_height()
			ax.annotate('{}'.format(height),
						xy=(rect.get_x() + rect.get_width() / 2, height),
						xytext=(offset[xpos] * 3, 3),  # use 3 points offset
						textcoords="offset points",  # in both directions
						ha=ha[xpos], va='bottom')

cAS = compareAStar()
cAS.runTest()