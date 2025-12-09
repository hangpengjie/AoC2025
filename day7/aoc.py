import sys
from itertools import accumulate
import bisect
sys.stdin = open('./day7/input.txt', 'r')
sys.stdout = open('./day7/output.txt', 'w')

def aoc_1():
    g = []
    try:
        while True:
            g.append(input())
    except EOFError:
        pass
    res = 0
    z = [g[0].index('S')]
    
    for i in range(1, len(g)):
        nxt = set()
        for pos in z:
            if g[i][pos] == '^':
                res += 1
                nxt.add(pos - 1)
                nxt.add(pos + 1)
            else:
                nxt.add(pos)
        z = nxt
    print(res)

def aoc_2():
    g = []
    try:
        while True:
            g.append(input())
    except EOFError:
        pass
    z = [0] * len(g[0])
    
    z[g[0].index('S')] += 1
    
    for i in range(1, len(g)):
        nxt = [0] * len(g[0])
        for pos in range(len(g[0])):
            if g[i][pos] == '^':
                nxt[pos - 1] += z[pos]
                nxt[pos + 1] += z[pos]
            else:
                nxt[pos] += z[pos]
        z = nxt
    print(sum(z))
aoc_2()