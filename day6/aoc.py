import sys
from itertools import accumulate
import bisect
sys.stdin = open('./day6/input.txt', 'r')
sys.stdout = open('./day6/output.txt', 'w')

def aoc_1():
    g = []
    try:
        while True:
            g.append(input())
    except EOFError:
        pass
    res = 0
    ops = g[-1].split()
    g = g[:-1]
    g = [list(map(int, s.split())) for s in g]
    for idx,op in enumerate(ops):
        if op == '+':
            cur = 0
            for i in range(len(g)):
                cur += g[i][idx]
            res += cur
        else:
            cur = 1 
            for i in range(len(g)):
                cur *= g[i][idx]
            res += cur
    print(res)
    
def aoc_2():
    g = []
    try:
        while True:
            g.append(input())
    except EOFError:
        pass
    res = 0
    ops = g[-1].split()
    g = g[:-1]
    point = 0
    def check():
        if point >= len(g[0]):
            return True
        return all(g[i][point] ==  ' ' for i in range(len(g)))
    for _,op in enumerate(ops):
        if op == '+':
            
            tot = 0
            while not check():
                cur = 0
                for i in range(len(g)):
                    if g[i][point] != ' ':
                        cur = cur * 10 + int(g[i][point]) 
                point += 1
                tot += cur
            res += tot
            point += 1
        else:
            
            tot = 1
            while not check():
                cur = 0
                for i in range(len(g)):
                    if g[i][point] != ' ':
                        cur = cur * 10 + int(g[i][point])
                point += 1
                tot *= cur
            res += tot
            point += 1
    print(res)
       
aoc_2()