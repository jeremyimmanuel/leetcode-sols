def minDistance(str1: str, str2: str) -> int:
    if str1 == str2:
        return 0

    if str1 == str2[::-1]:
        return len(str1)
    
    if str1 == '' or str2 == '':
        return max(len(str1), len(str2))

    m, n = len(str1), len(str2)

    # dp = [[-99] * (n+1)] * (m+1)
    dp = [ [ None for i in range(n + 1) ] for j in range(m + 1) ]

    for i in range(len(dp)):
        print(f'i : {i}')
        for j in range(len(dp[0])):
            print(f'j : {j}')
            if i == 0 or j == 0:
                print(f'assigning d[{i}][{j}] : {i + j}')
                dp[i][j] = i + j
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

def main():
    print(minDistance('heat', 'hit'))

if __name__ == "__main__":
    main()