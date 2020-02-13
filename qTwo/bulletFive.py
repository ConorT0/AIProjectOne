#conor is doing this
# this is currently broken. I am going to fix tomorrow.
import numpy as np
from matplotlib import pyplot as plt
import qOne.maze as maze
import qOne.AStarManhatten as AStarManhatten
import qOne.AStarEuclid as AStarEuclid
import qOne.bfs as bfs

class compareAStar(object):
	def __init__(self):
		self.p = .2
		self.dim = 100
		self.noMazes = 100
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
		ax.set_xticklabels(('Sum max fringe size', 'Sum of all nodes explored', 'Sum of path length'))
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

#m = maze.Maze(100,.2)
#m.gen_and_save_graphs_with_temp_path([(0,0)])
#man = AStarManhatten.AStarManhatten(m)
#resman = man.search()
#print(len(resman))

#m=maze.Maze(100,0)
#man = AStarManhatten.AStarManhatten(m)
#resman = man.search()
#print(len(resman))

#print(len(resman))

#m1 = maze.Maze(100,.2)

#man1 = AStarManhatten.AStarManhatten(m1)
#resman1 = man1.search()
#print(len(resman1))

#euclid = AStarEuclid.AStarEuclid(m)
#reseuclid = euclid.search()

#b = bfs.Bfs(m)
#resbfs = b.search()



#m.gen_and_save_graphs_with_temp_path(resman)
#print(len(resman))
#m.gen_and_save_graphs_with_temp_path(reseuclid)
#print(len(reseuclid))

#m.gen_and_save_graphs_with_temp_path(resbfs)
#print(len(resbfs))

##	print('uh oh')