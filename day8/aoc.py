import sys
from itertools import accumulate
import bisect
sys.stdin = open('./day8/input.txt', 'r')
sys.stdout = open('./day8/output.txt', 'w')

class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.sz = [1] * n
    def find(self, a):
        while a != self.p[a]:
            a = self.p[a]
        return a
    def merge(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.sz[a] < self.sz[b]:
            a, b = b, a
        self.p[b] = a
        self.sz[a] += self.sz[b]
        self.sz[b] = 0

def aoc_1():
    g = []
    try:
        while True:
            s = input().split(',')
            g.append(list(map(int, s)))
    except EOFError:
        pass
    dis = []
    for i in range(len(g)):
        for j in range(i + 1, len(g)):
            dis.append( (((g[i][0] - g[j][0]) ** 2 + (g[i][1] - g[j][1]) ** 2 + (g[i][2] - g[j][2]) ** 2), i, j))
    dis.sort()
    res = 0
    k = 1000
    uf = UF(len(g))
    for i in range(k):
        d, a, b = dis[i]
        uf.merge(a, b)
    uf.sz.sort()
    print(uf.sz[-1] * uf.sz[-2] * uf.sz[-3])

def aoc_2():
    g = []
    try:
        while True:
            s = input().split(',')
            g.append(list(map(int, s)))
    except EOFError:
        pass
    dis = []
    for i in range(len(g)):
        for j in range(i + 1, len(g)):
            dis.append( (((g[i][0] - g[j][0]) ** 2 + (g[i][1] - g[j][1]) ** 2 + (g[i][2] - g[j][2]) ** 2), i, j))
    dis.sort()
    res = 0
    uf = UF(len(g))
    i= 0
    cnt= 999
    while True:
        _, a, b = dis[i]
        if uf.find(a) != uf.find(b):
            cnt -= 1
            uf.merge(a, b)
        if cnt == 0:
            res = g[a][0] * g[b][0]
            break
        i += 1
    
    print(res)

aoc_2()