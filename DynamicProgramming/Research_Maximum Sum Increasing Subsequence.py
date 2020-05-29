"""https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/"""


def process():
    t = int(input().strip())
    while t != 0:
        t -= 1
        n = int(input().strip())
        arr = list(map(lambda x: int(x.strip()), input().strip().split()))
        i = 1
        maxarr = [i for i in arr]
        seq = [i for i in range(n)]
        while i < n:
            j = 0
            while j < i:
                if arr[i] > arr[j] and maxarr[i] < maxarr[j] + arr[i]:
                    maxarr[i] = maxarr[j] + arr[i]
                    seq[i] = j
                j += 1
            i += 1
        print(max(maxarr))


process()
