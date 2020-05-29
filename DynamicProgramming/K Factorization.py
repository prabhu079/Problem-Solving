'''https://www.hackerrank.com/challenges/k-factorization/problem'''

def main():
    n, k = list(map(lambda x: int(x), input().strip().split()))
    arr = list(map(lambda x: int(x), input().strip().split()))
    fact = []
    for i in arr:
        if n % i == 0:
            fact.append(i)
    fact = sorted(fact)
    l = len(fact)
    div = n
    res = [div]
    i = l - 1
    cd=0
    j=l-1
    while (i >= 0 and div != 1):
        while div % fact[i] == 0:
            div = div // fact[i]
            res.append(div)
            cd+=1
            j=i
        if i==1 and cd==1:
            div = n
            res = [div]
            i = j
            cd = 0
        i-=1

    try:
        res.index(1)
    except:
        res.append(1)
    res = res[::-1]
    if len(res) <= 2 or cd==1:
        print("-1")
    else:
        res = map(str, sorted(res))
        str1 = " ".join(res)
        print(str1)

main()
