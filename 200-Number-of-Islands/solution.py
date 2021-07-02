<<<<<<< HEAD
# Get number of islands
# 1. we want to do a bfs to search contiuous land (1)
# 2. when do we want to start the bfs though? every time we see an unvisited node

# Construct visited matrix
# Traverse through grid
# create queue for bfs purposes
# if 1 and unvisited:
#   start bfs

# bfs:
#   mark visited
#   get neighbours
#       for each neigbhour mark visited
#       get neighbour's neighbour

# everytime we see an unvisited land we enqueue after


=======
>>>>>>> 1a014af6b5b1e1b31f6e0b312428968754a847d2
from typing import List


def numIslands(grid: List[List[str]]) -> int:
<<<<<<< HEAD
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
=======
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ROWS, COLS = len(grid), len(grid[0])
    count = 0

    for r in range(ROWS):
        for c in range(COLS):
>>>>>>> 1a014af6b5b1e1b31f6e0b312428968754a847d2
            # found starting land
            if grid[r][c] == "1":
                count += 1

<<<<<<< HEAD
                # mark as visited
                grid[r][c] == "0"

                # construct queue
                neighbours = []
                # for starters append itself first
                neighbours.append((r, c))

                # while queue is not empty
                while len(neighbours) is not 0:
                    # get oldest node in the queue and dequeue it
                    i, j = neighbours.pop(0)

                    # up
                    if i - 1 >= 0 and grid[i - 1][j] == "1":
                        neighbours.append((i - 1, j))
                        grid[i - 1][j] = "0"
                    # down
                    if i + 1 < len(grid) and grid[i + 1][j] == "1":
                        neighbours.append((i + 1, j))
                        grid[i + 1][j] = "0"
                    # left
                    if j - 1 >= 0 and grid[i][j - 1] == "1":
                        neighbours.append((i, j - 1))
                        grid[i][j - 1] = "0"
                    # right
                    if j + 1 < len(grid[0]) and grid[i][j + 1] == "1":
                        neighbours.append((i, j + 1))
                        grid[i][j + 1] = "0"
=======
                queue = []
                queue.append((r, c))

                # while queue is not empty
                while len(queue) != 0:
                    row, col = queue.pop(0)
                    for d in directions:
                        neigh_row, neigh_col = row + d[0], row + d[1]
                        # check boundary and if land
                        if 0 <= neigh_row < ROWS and 0 <= neigh_col < COLS:
                            # set as visited
                            grid[neigh_row][neigh_col] = "0"
                            queue.append((neigh_row, neigh_col))

>>>>>>> 1a014af6b5b1e1b31f6e0b312428968754a847d2
    return count
