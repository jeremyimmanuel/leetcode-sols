# Graph DFS
# 1. Is it undirected or directed ? directed
# 2. Which direction flow should it follow ? Prereqs should point to the course
# 3. This is a cycle detection problem
# 4. This is a DFS problem
#   - base case: if node is `visiting` return false (then we see a cycle), if node is `visited` return true


from collections import defaultdict as dd
from enum import Enum
from typing import Dict, List


class DfsStatus(Enum):
    Unvisited = 0
    Visiting = -1
    Visited = 1


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    def dfs(course: int, visited: List[DfsStatus], adj_list: Dict) -> bool:
        if visited[course] == DfsStatus.Visiting.value:
            return False

        # if already visited in a previous pass, then this route is safe
        if visited[course] == DfsStatus.Visited.value:
            return True

        visited[course] = DfsStatus.Visiting.value
        # check if course is edge or not
        # if not edge
        if course in adj_list.keys():
            for next_course in adj_list[course]:
                if not dfs(next_course, visited, adj_list):
                    return False

        visited[course] = DfsStatus.Visited.value
        return True

    adj_list = dd(lambda: [])

    if len(prerequisites) <= 1:
        return True

    for p in prerequisites:
        course = p[0]
        prereq = p[1]
        adj_list[prereq].append(course)

    visited = [0 for _ in range(numCourses)]
    for node in range(numCourses):
        if not dfs(node, visited, adj_list):
            return False

    return True


def main():
    canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]])


if __name__ == "__main__":
    main()
