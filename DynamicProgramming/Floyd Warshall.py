import sys


def process():
    t = int(input().strip())
    while t != 0:
        t -= 1
        v = int(input().strip())
        adj = [[0 for _ in range(v)] for _ in range(v)]
        for i in range(v):
            adj[i] = list(map(lambda x: int(x.strip()) if x != "INF" else "INF", input().strip().split()))
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    if adj[i][k] != "INF" and adj[k][j] != "INF":
                        if adj[i][k] + adj[k][j] < adj[i][j]:
                            adj[i][j] = adj[i][k] + adj[k][j]
        #

        print(adj, sep=" ",end="")
        # print(str1, sep="", end="")


process()
