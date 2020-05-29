def main():
    n = int(input().strip())
    tails = [0] * n
    size = 0
    for p in tails:
        x = int(input().strip())
        low, high = 0, size
        while low != high:
            m = (low + high) // 2
            if tails[m] < x:
                low = m + 1
            else:
                high = m
        tails[low] = x
        size = max(low + 1, size)
    print(size)


main()
