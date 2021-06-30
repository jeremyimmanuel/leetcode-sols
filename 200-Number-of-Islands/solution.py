from typing import List


def numIslands(grid: List[List[str]]) -> int:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ROWS, COLS = len(grid), len(grid[0])
    count = 0

    for r in range(ROWS):
        for c in range(COLS):
            # found starting land
            if grid[r][c] == "1":
                count += 1

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

    return count
