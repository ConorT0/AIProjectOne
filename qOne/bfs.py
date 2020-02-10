import collections
import maze


class Bfs(object):
    def __init__(self, maze):  # takes in maze object
        self.maze = maze
        self.fringe = collections.deque()
        self.prev = [[None for j in range(maze.getDim())] for i in range(maze.getDim())]
        self.bfs()

    def bfs(self):
        path = []
        self.fringe.append((0, 0))  # add the starting point to the queue
        self.prev[0][0] = (0, 0)  # mark the starting point's previous as 0, 0 (for the path)
        while self.fringe:
            curr = self.fringe.popleft()  # remove first item in queue
            # if goal reached
            if curr == (self.maze.getDim() - 1, self.maze.getDim() - 1):
                print("Path found")  # trace back path and print
                gridCopy = [row[:] for row in self.maze.getGrid()]  # make copy of grid
                # using prev array, mark path with stars (not s or g)
                next = self.prev[curr[0]][curr[1]]  # next tuple in path
                path.append(next)
                while next != (0, 0):
                    gridCopy[next[0]][next[1]] = '*'
                    next = self.prev[next[0]][next[1]]  # next tuple in path
                    path.append(next)

                path.reverse()
                self.maze.updatePath(path)
                return

            neighbors = self.getValidNeighbors(curr)  # find all valid neighbors
            for n in neighbors:
                self.fringe.append(n)  # add all valid neighbors to queue
                self.prev[n[0]][n[1]] = curr  # mark previous nodes
        print("No solution found for: ")
        # self.maze.printGrid()

    def getValidNeighbors(self, curr):
        result = []  # initialize list for neighbors
        i = curr[0]  # row coordinate
        j = curr[1]  # column coordinate
        grid = self.maze.getGrid()

        # four neighbors: up, down, left, right
        # to be valid, must be in bounds, a free spot (==0), and not been visited yet (check prev array)

        # up: i - 1

        if i - 1 > -1 and (grid[i - 1][j] == 0 or grid[i - 1][j] == 'g') and self.prev[i - 1][j] is None:
            result.append((i - 1, j))

        # down: i + 1

        if i + 1 < len(grid) and (grid[i + 1][j] == 0 or grid[i + 1][j] == 'g') and self.prev[i + 1][j] is None:
            result.append((i + 1, j))

        # left: j - 1

        if j - 1 > -1 and (grid[i][j - 1] == 0 or grid[i][j - 1] == 'g') and self.prev[i][j - 1] is None:
            result.append((i, j - 1))

        # right: j + 1

        if j + 1 < len(grid) and (grid[i][j + 1] == 0 or grid[i][j + 1] == 'g') and self.prev[i][j + 1] is None:
            result.append((i, j + 1))

        return result


def printGridCopy(grid):
    for i in grid:
        print(*i, sep=" ")

if __name__ == '__main__':

    # test getValidNeighbors
    m = maze.Maze(100, 0.2)
    grid = m.getGrid()
    #m.printGrid()
    b = Bfs(m)
    # result = b.getValidNeighbors((1, 1))
    m.printGrid()
    # for item in result:
    #     print(item)
