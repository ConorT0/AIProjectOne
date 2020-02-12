from qOne import maze
from qOne import bfs
from qOne import dfs
from qOne import AStar
from qOne import AStarEuclid
from qOne import AStarManhatten
from qOne import bibfs

if __name__ == '__main__':

    # test getValidNeighbors
    m = maze.Maze(10, 0.2)

    # run each algorithm on the maze
    b = bfs.Bfs(m)
    m.printGrid()

    bib = bibfs.search(m)
    m.printGrid()

    d = dfs.search(m)
    m.printGrid()

    ae = AStarEuclid.search(m)
    m.printGrid()

    am = AStarManhatten.search(m)
    m.printGrid()