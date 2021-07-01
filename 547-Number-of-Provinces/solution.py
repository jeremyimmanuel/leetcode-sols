"""
Graph, undirected,
1. BFS? DFS? I think it's DFS
2. Iterate through matrix
3. Cycles are okay
4. build adj matrix
5. iterate through 0 to n - 1
      - for each city we explore the neighbour
          if not visited yet:
            dfs:
                mark it as visited
                stop when evey neighbour is visited or doesn't have any more neighbours left
            province count ++
   return province count
"""

from collections import defaultdict as dd
from typing import Dict, List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # build adj dictionary
        adj = dd(lambda: [])

        # o(n^2)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    adj[i].append(j)

        visited = [False for _ in range(len(isConnected))]

        def dfs(city: int, visited: List[bool], adj: Dict) -> None:
            # base case
            if visited[city]:
                return

            # recursive case
            visited[city] = True
            for neighbour in adj[city]:
                dfs(neighbour, visited, adj)
            return

        count = 0
        for city in range(len(isConnected)):
            if not visited[city]:
                dfs(city, visited, adj)
                count += 1
        return count
