import sys
from itertools import accumulate
import bisect
import queue
from functools import lru_cache
from collections import defaultdict
import pulp
sys.stdin = open('./day11/input.txt', 'r')
sys.stdout = open('./day11/output.txt', 'a')
def aoc_1():
    g = defaultdict(list)
    
    try:
        while True:
            s = input().split(': ')
            g[s[0]].extend(s[1].split())
    except EOFError:
        pass
    res = 0
    start = 'you'
    end = 'out'
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        for v in g[u]:
            if v == end:
                res += 1
            else:
                q.put(v)
    print(res)

def aoc_2():
    g = defaultdict(list)
    
    try:
        while True:
            s = input().split(': ')
            g[s[0]].extend(s[1].split())
    except EOFError:
        pass
    @lru_cache(None)
    def dfs(v,v1,v2):
        if  v == 'out':
            if v1 and v2:
                return 1
            return 0
        if v == 'fft':
            v1 = 1
        if v == 'dac':
            v2 = 1
        return sum(dfs(nv,v1,v2) for nv in g[v])
    print(dfs('svr',0,0))
    
aoc_2()