from collections import defaultdict as dd
from typing import Dict, List


def countComponents(n: int, edges: List[List[int]]) -> int:
    def traverse(node: int, visited: List[int], adj: Dict) -> None:
        visited[node] = True

        for neigh in adj[node]:
            if not visited[neigh]:
                traverse(neigh, visited, adj)

    adj = dd(list)

    for edge in edges:
        a, b = edge[0], edge[1]
        adj[a].append(b)
        adj[b].append(a)

    visited = [False for _ in range(n)]
    count = 0
    for node in range(n):
        if not visited[node]:
            traverse(node, visited, adj)
            count += 1

    return count
