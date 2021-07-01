"""
Solution from leetcode
"""
from collections import defaultdict as dd
from typing import Dict, List
from enum import Enum


class Graph(Enum):
    Unvisited = 0
    Visited = 1
    Visiting = -1


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Let G(V, E) -> directed, unweighted graph
    """

    def is_good(course, visited: List[Graph], adj: Dict, stack: List) -> bool:
        if visited[course] == Graph.Visited:
            return True
        if visited[course] == Graph.Visiting:
            return False

        visited[course] = Graph.Visiting

        for neighbour in adj[course]:
            if not is_good(neighbour, visited, adj, stack):
                return False
        stack.append(course)
        visited[course] = Graph.Visited
        return True

    adj = dd(lambda: [])
    for pair in prerequisites:
        course = pair[0]
        prereq = pair[1]
        adj[prereq] = course
    visited = [Graph.Unvisited for _ in range(numCourses)]
    stack = []

    for course in range(numCourses):
        if not is_good(course, visited, adj, stack):
            return []

    return stack[::-1]


def main():
    pass


if __name__ == "__main__":
    pass
