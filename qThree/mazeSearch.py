from qOne import maze
# My approach for making harder mazes will be very simple: instead of definining neighbors as the same node with another
# block added anywhere in random walk, neighbors will be a block added in the path that the algo took.
# All neighbors would be each cell in the path blocked. For example, if the path is of length 10, then there will be
# 10 neighbors, each one with a different cell blocked.
#
import pickle
import threading
import heapq
from qThree import mazeNeighbor
from qOne import maze
from qOne import dfs
from qOne import AStarManhatten


class mazeEnhancer(object):
	def __init__(self, noMazes: int, dim: int):
		self.imnumber=0
		self.dim = dim
		self.type = False  # true for bfs, false for ASTAR
		self.mazes = []
		self.noMazes = noMazes
		self.changeThreshhold = 1
		self.stopAfterBeingUnderThresholdThisManyTimes=25
		x = 0
		while (x < noMazes):
			m = maze.Maze(dim, .2)
			if self.type:
				if self.rankDFS(m) != 0:
					self.mazes.append(m)
					x += 1
			else:
				if self.rankAstar(m) != 0:
					self.mazes.append(m)
					x += 1
		self.running = True
		heapq.heapify(self.mazes)

	def rankDFS(self, m:maze.Maze) -> int:
		d = dfs.Dfs(m)
		path = d.search()
		if path is None:
			return 0
		m.gen_and_save_graphs_with_temp_path(path,fname=str(self.imnumber))
		self.imnumber+=1
		m.rank = d.get_max_fringe()
		return d.get_max_fringe()

	def rankAstar(self, m:maze.Maze) -> int:
		aStar = AStarManhatten.AStarManhatten(m)
		path = aStar.search()
		if path is None:
			return 0
		m.gen_and_save_graphs_with_temp_path(path,fname=str(self.imnumber))
		self.imnumber+=1
		m.rank = aStar.getNodesExplored()
		return aStar.getNodesExplored()

	def explore(self):
		old = 0 # the score of the last maze.
		numbertimesunderthreshhold=0
		while numbertimesunderthreshhold<self.stopAfterBeingUnderThresholdThisManyTimes:
			i = 0

			while i<3: # every dim iterations, save what the maze looks like

				maxn = []
				for j in range(self.noMazes): # for each maze, explore it's neighbors
					maze = self.mazes[j]
					topNeighborExplorer = mazeNeighbor.mazeNeightborManager(maze, self.type, self.noMazes)
					topneighbors = topNeighborExplorer.getMaxNeightbor()
					if len(topneighbors) !=0:
						newMaze = heapq.heappop(topneighbors)
						self.mazes[j] = max(newMaze,self.mazes[j])

					maxn.append(topneighbors)
					heapq.heapify(self.mazes)
				#maxitem = maxn[0][-1]
				#for item in maxn: # out of all the neighbor's we just explored, find the best of the best.
				#	maxitem = max(item[-1], maxitem)
				#if maxitem >= self.mazes[0]:  # if the best of the best neighbor is better than the worst current maze
				#	heapq.heappop(self.mazes) # replace it
				#	heapq.heappush(self.mazes, maxitem)
				i+=1
			for m in self.mazes:
				if(self.type):
					self.rankDFS(m)
				else:
					self.rankAstar(m)

			print('done with one loop, current max is ' + str(self.mazes[-1].rank))
			if self.mazes[-1].rank - old < self.changeThreshhold:
				numbertimesunderthreshhold+=1
			else:
				numbertimesunderthreshhold = 0
			old = self.mazes[-1].rank

		#we are done, time to save the maze
		file = open('maze.obj', 'wb')
		pickle.dump(self.mazes, file)




if __name__ == '__main__':
	m = mazeEnhancer(2,30)
	m.explore()

