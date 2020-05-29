"""https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0"""


def process():
    t = int(input().strip())
    while t != 0:
        t -= 1
        n1, n2 = list(map(lambda x: int(x.strip()), input().strip().split()))
        str1 = input().strip()
        str2 = input().strip()
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        print(dp[n1][n2])


process()
