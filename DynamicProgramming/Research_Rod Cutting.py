"""https://practice.geeksforgeeks.org/problems/rod-cutting/0"""


def process():
    t = int(input().strip())
    while t != 0:
        t -= 1
        n = int(input().strip())
        arr = list(map(lambda x: int(x.strip()), input().strip().split()))
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                dp[j] = max(dp[j], dp[j - i] + arr[i - 1])
        print(dp[n])


process()
