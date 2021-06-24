"""
Graph Problem
1. Is it directed or undirected? directed
2. Either dfs or bfs, dfs
3. Setup? Setup the phone dictionary + adj list?
4. Setting up phone dict -> ez
5. Setting adj list -> tricky
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict: Dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": "g h i".split(),
            "5": "j k l".split(),
            "6": "m n o".split(),
            "7": "p q r s".split(),
            "8": "t u v".split(),
            "9": "w x y z".split(),
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return phone_dict[digits]

        adj = {}
        for i in range(len(digits) - 1):
            letter_arr = phone_dict[digits[i]]
            for letter in letter_arr:
                adj[letter] = phone_dict[digits[i + 1]]

        ans = []

        def dfs(letter, s, ans, adj):
            # this function will fill ans
            # base case -> if node is edge
            if letter not in adj.keys():
                ans.append(s)

            # recursive case
            for next_letter in adj[letter]:
                dfs(next_letter, s + next_letter, ans, adj)

        for starting_letter in phone_dict[digits[0]]:
            dfs(starting_letter, "", ans, adj)
        print(ans)
        return ans
