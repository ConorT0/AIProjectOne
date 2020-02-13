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
    b = bfs.Bfs(m).bfs()
    print("BFS:")
    m.print_with_temp_path(b)
    print()

    bib = bibfs.BiDirectionalBFS(m).search()
    print("Bidirectional BFS:")
    m.print_with_temp_path(bib)
    print()

    d = dfs.Dfs(m).search()
    print("DFS:")
    m.print_with_temp_path(d)
    print()

    ae = AStarEuclid.AStarEuclid(m).search()
    print("AStar (Euclidean Heuristic):")
    m.print_with_temp_path(ae)
    print()

    am = AStarManhatten.AStarManhatten(m).search()
    print("AStar (Manhattan Heuristic):")
    m.print_with_temp_path(am)
    print()