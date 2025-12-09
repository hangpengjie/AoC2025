import sys
from itertools import accumulate
import bisect
sys.stdin = open('./day5/input.txt', 'r')
sys.stdout = open('./day5/output.txt', 'w')

def aoc_1():
    g = []
    q = []
    try:
        while True:
            s = input()
            if s == '':
                break
            s = s.split('-')
            g.append((int(s[0]), int(s[1])))
        while True:
            s = input()
            q.append(int(s))
    except EOFError:
        pass
    res = 0
    g.sort()
    z = []
    for l,r in g:
        if z and z[-1][1] >= l:
            z[-1][1] = max(z[-1][1], r)
        else:
            z.append([l,r])
    z =  [tuple(x) for x in z]
    for c in q:
        idx  = bisect.bisect_right(z, (c, float('inf'))) - 1
        if idx  >= 0 and z[idx][0] <= c <= z[idx][1]:
            res += 1

    print(res)

def aoc_2():
    g = []
    q = []
    try:
        while True:
            s = input()
            if s == '':
                break
            s = s.split('-')
            g.append((int(s[0]), int(s[1])))
        while True:
            s = input()
            q.append(int(s))
    except EOFError:
        pass
    res = 0
    g.sort()
    z = []
    for l,r in g:
        if z and z[-1][1] >= l:
            z[-1][1] = max(z[-1][1], r)
        else:
            z.append([l,r])
    for l,r in z:
        res += r - l + 1

    print(res)

# aoc_1()
aoc_2()