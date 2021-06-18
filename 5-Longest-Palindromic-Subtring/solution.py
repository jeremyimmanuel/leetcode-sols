def longestPalindrome(s: str) -> str:
    dp = [[None for _ in range(len(s))] for _ in range(len(s))]

    ans = 1
    for i in len(s):
        for j in len(s):
            if i is j:
                dp[i][j] = True
            if i + 1 is j:
                dp[i][j] = s[i] is s[j]
    for i in len(s) - 2:
        for j in range(i + 2, len(s)):
            dp[i][j] = dp[i + 1][j - 1] and s[i] is s[j]
            if dp[i][j]:
                ans = max(ans, j - 1 + 1)
    return ans
