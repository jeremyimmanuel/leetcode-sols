"""
Graph Problem
1. Is it directed or undirected? directed
2. Either dfs or bfs, dfs
3. Setup? Setup the phone dictionary + adj list?
4. Setting up phone dict -> ez
5. Setting adj list -> tricky
"""

from typing import Dict, List
from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict: Dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        return []
