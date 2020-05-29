"""https://practice.geeksforgeeks.org/problems/negative-weight-cycle/0"""
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.wt = weight


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, data):
        if None is self.first:
            self.first = Node(data)
            self.last = self.first
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def delete(self):
        if None is self.first:
            print("Queue is Empty!!!!")
            return None
        else:
            data = self.first.data
            self.first = self.first.next
            return data

    def is_empty(self):
        return None is self.first


def process():
    t = int(input().strip())
    while t != 0:
        t -= 1
        v, e = list(map(lambda x: int(x.strip()), input().strip().split()))
        # adj = [[0 for _ in range(v)] for _ in range(v)]
        lst = list(map(lambda x: int(x.strip()), input().strip().split()))
        i = 0
        edges = []
        for j in range(e):
            edge = Edge(lst[i], lst[i + 1], lst[i + 2])
            edges.append(edge)
            i += 3
        del lst
        maxv = sys.maxsize
        d = [maxv for _ in range(v + 1)]
        d[0] = 0
        sl = False
        p = [0 for _ in range(v + 1)]
        for i in range(v):
            if sl:
                break
            for j in range(e):
                u = edges[j].src
                v = edges[j].dest
                wt = edges[j].wt
                if u == v and wt < 0:
                    sl = True
                    print(1)
                    break
                if d[u] != maxv and d[v] > d[u] + wt:
                    d[v] = d[u] + wt
                    p[v] = u
        for j in range(e):
            if sl:
                break
            u = edges[j].src
            v = edges[j].dest
            wt = edges[j].wt
            if d[u] != maxv and d[v] > d[u] + wt:
                print("1")
                break
            else:
                print("0")
                break


process()