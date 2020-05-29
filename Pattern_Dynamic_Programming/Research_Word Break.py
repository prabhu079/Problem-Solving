"""https://practice.geeksforgeeks.org/problems/word-break/0"""


def process():
    t = int(input().strip())
    while t != 0:
        t -= 1
        n = int(input().strip())
        arr = list(map(lambda x: x.strip(), input().strip().split()))
        dict1 = {}
        for val in arr:
            dict1[val] = True
        del arr
        str1 = input().strip()
        l = len(str1)
        dp = [[False for _ in range(l)] for _ in range(l)]
        for i in range(l):
            j = 0
            k = i
            while j < l and k < l:
                tstr = str1[j:k + 1]
                tl = len(tstr)
                if dict1.get(tstr):
                    dp[j][k] = True
                else:
                    for t1 in range(tl):
                        tstr1 = tstr[0:t1 + 1]
                        tstr2 = tstr[t1 + 1:]
                        if (dict1.get(tstr1) is not None and dict1.get(tstr2) is not None) or (
                                j + t1 < l - 1 and dp[j][j + t1] and dp[j + t1 + 1][k]):
                            dp[j][k] = True
                j += 1
                k += 1
        if dp[0][l - 1]:
            print("1")
        else:
            print("0")


process()
