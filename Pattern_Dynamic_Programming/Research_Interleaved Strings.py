"""https://practice.geeksforgeeks.org/problems/interleaved-strings/1"""


def isInterleave(a, b, c):
    if len(a) + len(b) != len(c):
        return False
    elif (a + b) == c or (b + a) == c:
        return True
    cnt1 = [0 for _ in range(26)]
    temp = a + b
    for i in temp:
        ind = ord(i) - ord('a')
        cnt1[ind] += 1

    cnt2 = [0 for _ in range(26)]
    for i in c:
        ind = ord(i) - ord('a')
        cnt2[ind] += 1
    print(cnt1)
    print(cnt2)

    for i in range(26):
        if cnt1[i] != cnt2[i]:
            return False
    lc = len(a) + 1
    lr = len(b) + 1
    dp = [[False for _ in range(lc)] for _ in range(lr)]
    dp[0][0] = True
    for j in range(1, lc):
        if c[j - 1] == a[j - 1] and dp[0][j - 1]:
            dp[0][j] = True

    for j in range(1, lr):
        if c[j - 1] == b[j - 1] and dp[j - 1][0]:
            dp[j][0] = True

    for i in range(1, lr):
        for j in range(1, lc):
            if (c[i + j - 1] == a[j - 1] or c[i + j - 1] == b[i - 1]) and (dp[i - 1][j] or dp[i][j - 1]):
                dp[i][j] = True
    return dp[lr - 1][lc - 1]


def process():
    t = int(input().strip())
    while t != 0:
        t -= 1
        a, b, c = input().strip().split()
        print("1") if isInterleave(a, b, c) else print("0")


process()
