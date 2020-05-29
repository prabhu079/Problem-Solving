"""https://practice.geeksforgeeks.org/problems/number-of-coins/0"""


def swap(arr, left, right):
    t = arr[left]
    arr[left] = arr[right]
    arr[right] = t


def partition(arr, low, high):
    piv = arr[low]
    left = low
    right = high
    while left < right:
        while left < high and arr[left] >= piv:
            left += 1
        while right > low and arr[right] <= piv:
            right -= 1
        if left < right:
            swap(arr, left, right)
    # the swap will be based on this below if condition only
    if right > low:
        swap(arr, right, low)
    return right


def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)


def process():
    mval = 10 ** 6 + 1
    t = int(input().strip())
    while t != 0:
        t -= 1
        v, n = list(map(lambda x: int(x.strip()), input().strip().split()))
        arr = list(map(lambda x: int(x.strip()), input().strip().split()))
        dp = [mval for _ in range(v + 1)]
        # quickSort(arr, 0, n - 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(arr[i - 1], v + 1):
                if dp[j - arr[i - 1]] != mval:
                    dp[j] = min(dp[j], dp[j - arr[i - 1]] + 1)
        print(dp[v]) if dp[v] != mval else print("-1")


process()
