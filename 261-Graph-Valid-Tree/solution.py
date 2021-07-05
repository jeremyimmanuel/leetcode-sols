"""
What is a valid tree?

No cycle == valid tree
Cycle detection problem

Graph, undirected, unweighted

Build adj list

Dfs
Unvisited, Visiting, Visited

dfs(from, n, visited, adj):
    # base case
    if visited[n] == Visited:
        return True
    if visited[n] == Visiting:
         return False
    visited[n] = Visiting
    for neigh in adj[n]:
        if neigh is from:
            skip
        else:
            is_safe = dfs(from=n, neigh, visited, adj)
            if is_safe is False:
                return False
    visited[n] = Visited
    return True

0 - 1

2 - 3
"""
from collections import defaultdict as dd
from typing import Dict, List


def validTree(n: int, edges: List[List[int]]) -> bool:
    adj_list = dd(list)

    # space o(n + m)
    for edge in edges:
        a, b = edge[0], edge[1]
        adj_list[a].append(b)
        adj_list[b].append(a)
    # space o(n)
    visited = ["Unvisited" for _ in range(n)]

    # runtime o(n) because touching every route
    def dfs(prev: int, curr: int, visited: List[str], adj: Dict) -> bool:
        # base case
        if visited[curr] == "Visited":
            return True
        if visited[curr] == "Visiting":
            return False

        # set to visiting
        visited[curr] = "Visiting"

        for neigh in adj[curr]:
            if neigh == prev:
                continue
            is_safe = dfs(curr, neigh, visited, adj)
            if not is_safe:
                return False
        # when finished traversing through graph,
        # set to viisted
        visited[curr] = "Visited"
        return True

    check = dfs(None, 0, visited, adj_list)
    if not check:
        return False

    # there's a separeate graph
    if "Unvisited" in visited:
        return False

    # total space is o(n + m), where n is the nodes and m is n's neighbours
    return True
