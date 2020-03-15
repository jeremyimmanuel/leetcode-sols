'''
Solution from Kagaya John
https://www.youtube.com/watch?v=Y0KEUZ1C4YY
'''

from collections import defaultdict as dd
from typing import List

def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    # base case
    if n == 1:
        return [0]
    
    # add default dict with a default action of set
    # nb for neighbours
    nb = dd(set)

    for u, v in edges:
        nb[u].add(v)
        nb[v].add(u)
    
    # add all leaves to pre-level
    pre_level, unvisited = [], set()
    for i in range(n):
        # if leaf
        if len(nb[i]) == 1:
            pre_level.append(i)
        unvisited.add(i)

    # a graph can have at most 2 MHTS
    # BFS from leaves until 
    while len(unvisited) > 2:
        cur_level = []
        for u in pre_level:
            print(f'current node : {u}')
            unvisited.remove(u)
            # check every neighbour of currNode
            for v in nb[u]:
                print(f'node {u} -> {v}')
                if v in unvisited:
                    print(f'node {v} is unvisited')
                    nb[v].remove(u)
                    # if v is a leave, len(nb[v]) would be 0
                    # if not we put it in the next level
                    if len(nb[v]) == 1:
                        cur_level.append(v)
        pre_level = cur_level

    print(f'unvisited length : {len(unvisited)}')
    return list(unvisited)

def test1():
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    ans = [1]
    assert findMinHeightTrees(n, edges) == ans

def test2():
    n = 6
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    ans = [3, 4]
    assert findMinHeightTrees(n, edges) == ans


def main():
    print('Testing test1...\n')
    test1()
    print()
    print('Testing test2...\n')
    test2()
    


if __name__ == '__main__':
    main()
