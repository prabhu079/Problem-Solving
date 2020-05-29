"""https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0"""


def optimizeProcess():
    t = int(input().strip())
    while t != 0:
        t -= 1
        n = int(input().strip())
        mw = int(input().strip())
        values = list(map(lambda x: int(x.strip()), input().strip().split()))
        weights = list(map(lambda x: int(x.strip()), input().strip().split()))
        dp = [0 for _ in range(mw + 1)]
        for i in range(n):
            for j in range(mw, weights[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
        print(dp[mw])


def process():
    t = int(input().strip())
    while t != 0:
        t -= 1
        n = int(input().strip())
        mw = int(input().strip())
        values = list(map(lambda x: int(x.strip()), input().strip().split()))
        weights = list(map(lambda x: int(x.strip()), input().strip().split()))
        dp = [[0 for _ in range(mw + 1)] for _ in range(n)]
        for i in range(n):
            for j in range(1, mw + 1):
                if i == 0:
                    dp[i][j] = 0 if j < weights[0] else values[0]
                else:
                    if j < weights[i]:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = max(dp[i - 1][j], (dp[i - 1][j - weights[i]] + values[i]))
        print(dp[n - 1][mw])


optimizeProcess()
# process()
