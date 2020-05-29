"""https://practice.geeksforgeeks.org/problems/palindromic-patitioning/0"""


def process():
    t = int(input().strip())
    while t != 0:
        t -= 1
        s = input().strip()
        n = len(s)
        maxv = n
        cnt = 0
        dp = [[maxv for _ in range(n + 1)] for _ in range(n + 1)]
        for k in range(1, n + 1):
            i = 1
            j = k
            while j <= n and i <= n:
                str1 = s[i - 1:j]
                if str1 == str1[::-1]:
                    dp[i][j] = 0
                else:
                    for m in range(i, j):
                        if dp[i][m] != maxv and dp[m+1][j] != maxv:
                            dp[i][j] = min(dp[i][j], 1 + dp[i][m] + dp[m+1][j])
                i += 1
                j += 1

        print(dp[1][n])


process()
