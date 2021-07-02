# points = [[3,3],[5,-1],[-2,4]], k = 2
# points[0] -> sqrt(18)
# points[1] -> sqrt(26)
# points[2] -> sqrt(20)

# 1. calc distance using euqlidian
# 2. sort it

from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    if len(points) == 0:
        return []

    if k == len(points):
        return points

    # runtime: O(NlogN)
    # space: o(n + k)
    return sorted(points, key=lambda pair: (pair[0]) ** 2 + (pair[1]) ** 2)[:k]
