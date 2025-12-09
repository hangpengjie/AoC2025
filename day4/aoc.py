import sys
from itertools import accumulate
sys.stdin = open('./day4/input.txt', 'r')
sys.stdout = open('./day4/output.txt', 'w')

def aoc_1():
    g = []
    try:
        while True:
            g.append(input())
    except EOFError:
        pass
    res = 0
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    m,n = len(g), len(g[0])
    for i in range(m):
        for j in range(n):
            if g[i][j] == '.':
                continue
            cnt = 0
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and g[x][y] == '@':
                    cnt += 1
            if cnt < 4:
                res += 1
    print(res)
                    
def aoc_2():
    g = []
    try:
        while True:
            g.append(list(input()))
    except EOFError:
        pass
    res = 0
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    m,n = len(g), len(g[0])
    change = True
    while change:
        change = False
        for i in range(m):
            for j in range(n):
                if g[i][j] == '.':
                    continue
                cnt = 0
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and g[x][y] == '@':
                        cnt += 1
                if cnt < 4:
                    g[i][j] = '.'
                    res += 1
                    change = True
    print(res)
aoc_2()