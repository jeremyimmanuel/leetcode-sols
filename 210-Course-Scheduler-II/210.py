'''
Solution from leetcode
'''
from collections import defaultdict as dd
from enum import Enum

class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3

def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    '''
    Let G(V, E) -> directed, unweighted graph
    '''
    # [a, b] = b->a

    adjMat = dd(list)
    for after, before in prerequisites:
        adjMat[before].append(after)
    
    stack = []
    visited = set()
    possible = True
    color = {k: Color.WHITE for k in range(numCourses)}

    def dfs(node):
        nonlocal possible

        if not possible:
            return

        color[node] = Color.GRAY

        # check if node in key list
        if node in ajdMat:
            for v in adjMat[node]:
                if color[v] == Color.WHITE:
                    dfs(v)
                elif color[v] == Color.GRAY:
                    possible = False

        # Recursion ends. Mark as black
        color[node] = Color.BLACK
        stack.append(node)
    
    for vertex in range(numCourses):
        if color[vertex] == Color.WHITE:
            dfs(vertex)
    
    return stack[::-1] if possible else []

    # for u in range(numCourses):
    #     if u in visited:
    #         continue
    #     for v in adjMat[u]:
    #         if v in visited:
    #             continue
    #         # cannot go anywhere
    #         if len(adjMat[v]) == 0:
    #             stack.append(v)
    #             visited.add(v)

    #     stack.append(u)
    #     visited.add(u)


def main():
    pass

if __name__ == "__main__":
    pass