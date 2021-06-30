"""
How many iteration till everything is rotten, if possible

If impossible to contaminate every oranges, return -1

1. Count fresh oranges
2. Graphs, undirected, unweighted
3. DFS or BFS? BFS
"""
from collections import deque
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    ROTTEN = 2
    FRESH = 1
    EMPTY = 0

    queue = deque()

    # 1. Count fresh oranges and put rottens in the queue
    fresh_oranges = 0
    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):
            # rotten
            if grid[r][c] == ROTTEN:
                queue.append((r, c))
            # fresh
            elif grid[r][c] == FRESH:
                fresh_oranges += 1

    minutes_elapsed = -1
    queue.append((-1, -1))
    # up  # right  # down  # left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while len(queue) != 0:
        row, col = queue.popleft()
        if row == -1:
            minutes_elapsed += 1

            # if there's still elements in the queue then
            # add another delimiter because there's still another level
            if len(queue) != 0:
                queue.append((-1, -1))
        else:
            for d in directions:
                neigh_row, neigh_col = row + d[0], col + d[1]

                # check boundary
                if 0 <= neigh_row < ROWS and 0 <= neigh_col <= COLS:
                    if grid[neigh_row][neigh_col]:
                        grid[neigh_row][neigh_col] = ROTTEN
                        fresh_oranges -= 1
                        queue.append((neigh_row, neigh_col))

    return minutes_elapsed if fresh_oranges == 0 else -1
