"""https://practice.geeksforgeeks.org/problems/coin-change/0/"""


def process():
    t = int(input().strip())
    while t != 0:
        t -= 1
        m = int(input().strip())
        arr = list(map(lambda x: int(x.strip()), input().strip().split()))
        v = int(input().strip())
        dp = [0 for _ in range(v + 1)]
        dp[0] = 1
        for i in range(1, m + 1):
            for j in range(arr[i - 1], v + 1):
                dp[j] += dp[j - arr[i - 1]]
        print(dp[v])


process()
