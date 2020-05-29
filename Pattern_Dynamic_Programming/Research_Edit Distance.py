"""https://practice.geeksforgeeks.org/problems/edit-distance/0"""


def process():
    t = int(input().strip())
    while t != 0:
        t -= 1
        l1, l2 = map(lambda x: int(x.strip()), input().strip().split())
        str1, str2 = map(lambda x: x.strip(), input().strip().split())
        l1, l2 = l1 + 1, l2 + 1
        dp = [[0 for x in range(l2)] for _ in range(l1)]
        for i in range(0, l1):
            for j in range(0, l2):
                if i == 0 or j == 0:
                    dp[i][j] = max(i, j)
                else:
                    if str1[i - 1] == str2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        print(dp[l1 - 1][l2 - 1])


process()
