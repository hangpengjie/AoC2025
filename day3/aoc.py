import sys
from itertools import accumulate
sys.stdin = open('./day3/input.txt', 'r')
sys.stdout = open('./day3/output.txt', 'w')

def aoc_1():
    g = []
    try:
        while True:
            g.append(input())
    except EOFError:
        pass
    res = 0
    for x in g:
        t = [0] * 10
        mx = 0
        for c in x:
            for i in range(9,  -1, -1):
                if t[i] > 0:
                    mx = max(mx, i *  10 + int(c))
                    break
            t[int(c)] += 1
        res += mx
    print(res)
def aoc_2():
    g = []
    try:
        while True:
            g.append(input())
    except EOFError:
        pass
    res = 0
    
    def ops(x):
        length = len(x)
        cur = [0] * 12
        
        for i in range(length):
            digit = int(x[i])
            left = min(length - i - 1, 11)
            while left >= 0 and cur[left] >= digit:
                left -= 1
            if left >= 0:
                cur[left] = digit
                for j in range(left):
                    cur[j] = 0
        nonlocal res
        res += int(''.join(map(str, cur[::-1])))


    for x in g:
        ops(x)
    print(res)

aoc_2()