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


from typing import List


def numIslands(grid: List[List[str]]) -> int:
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # found starting land
            if grid[r][c] == "1":
                count += 1

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
    return count
