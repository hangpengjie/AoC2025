import sys
from itertools import accumulate
sys.stdin = open('./day2/input.txt', 'r')
sys.stdout = open('./day2/output.txt', 'w')

def aoc_1():
    l,r = [],[]
    try:
        while True:
            s = input().split(',')
            for x in s:
                z = x.split('-')
                l.append(int(z[0]))
                r.append(int(z[1]))
    except EOFError:
        pass
    
    def dfs(cur, high):
        x = int(str(cur) + str(cur))
        if x > high:
            return 0
        ans = x
        for i in range(10):
            if cur == 0 and i == 0: continue
            ans += dfs(cur * 10 + i, high)
        return ans
    res = 0
    for i in range(len(l)):
        res += dfs(0, r[i]) - dfs(0, l[i]-1)
    print(res)

def aoc_2():
    l,r = [],[]
    try:
        while True:
            s = input().split(',')
            for x in s:
                z = x.split('-')
                l.append(int(z[0]))
                r.append(int(z[1]))
    except EOFError:
        pass
    z = set()
    def dfs(cur, low, high):
        x = int(str(cur) + str(cur))
        if x > high:
            return 0
        ans = 0
        
        while x <= high and x != 0:
            if x >= low: z.add(x)
            ans += x
            x = int(str(x) + str(cur))
        for i in range(10):
            if cur == 0 and i == 0: continue
            ans += dfs(cur * 10 + i, low, high)
        return ans
    res = 0
    for i in range(len(l)):
        z.clear()
        dfs(0, l[i], r[i])
        res += sum(z)
    print(res)

aoc_2()