'''https://www.hackerrank.com/challenges/stockmax/problem'''


def main():
    t = int(input().strip())
    while t > 0:
        n = int(input().strip())
        arr = list(map(lambda x: int(x.strip()), input().strip().split()))
        profit = 0
        first = 0
        ind = 0
        while ind != n - 1:
            if first != n - 1:
                maxEle = max(arr[first:n])
            else:
                maxEle = arr[first]
            ind = n - 1 - arr[::-1].index(maxEle)
            profit = max(profit, profit + ((ind - first) * arr[ind]) - sum(arr[first:ind]))
            first = ind + 1

        print(profit)
        t -= 1


main()
