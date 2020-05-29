"""https://practice.geeksforgeeks.org/problems/nth-catalan-number/0"""


def process():
    t = int(input().strip())
    while t != 0:
        t -= 1
        n = int(input().strip())
        c = [0 for _ in range(n + 1)]
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        c[0] = 1
        for cn in range(1, n + 1):
            j = cn - 1
            i = 0
            while i < cn and j >= 0:
                c[cn] += (c[i] * c[j])
                i += 1
                j -= 1
            i = 0
            j = cn
            while j >= 0 and i <= cn:
                dp[j][i] = c[j] * c[i]
                dp[i][j] = dp[i][j]
                i += 1
                j -= 1
        print(c[n])


process()
