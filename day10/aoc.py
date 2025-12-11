import sys
from itertools import accumulate
import bisect
import pulp
sys.stdin = open('./day10/input.txt', 'r')
sys.stdout = open('./day10/output.txt', 'a')
def aoc_1():
    g = []
    q = []
    try:
        while True:
            s = input().split()[:-1]
            tar = 0
            n  = len(s[0][1:-1])
            for ch  in s[0][1:-1]:
                tar *= 2
                if ch == '#':
                    tar += 1
            g.append(tar)
            z = []
            s = s[1:]
            for c in s:
                c = c[1:-1]
                cur = 0
                for d in map(int, c.split(',')):
                    cur = cur | (1 << (n-1-d))
                z.append(cur)
            q.append(z)
    except EOFError:
        pass
    def min_ops(tar, ops):
        cnt = float('inf')
        n = len(ops)
        for i in range(1 << n):
            cur = 0
            for j in range(n):
                if i & (1 << j):
                    cur = cur ^ ops[j]
            if cur == tar:
                cnt = min(cnt, bin(i).count('1'))
        return cnt
    res = sum(min_ops(g[i], q[i]) for i in range(len(g)))
    print(res)


def aoc_2():
    g = []
    q = []
    try:
        while True:
            s = input().split()
            g.append(list(map(int, s[-1][1:-1].split(','))))
            s = s[1:-1]
            q.append([list(map(int, c[1:-1].split(','))) for c in s])
    except EOFError:
        pass
    for x in q:
        x.sort(key=lambda a: -len(a))
    res = 0
    
    for i in range(len(g)):
        num_buttons = len(q[i])
        num_leds = len(g[i]) 
        prob = pulp.LpProblem("Minimize_Buttons", pulp.LpMinimize)
        x = [pulp.LpVariable(f"x_{i}", lowBound=0, cat="Integer") for i in range(num_buttons)]
        for j in range(num_leds):
            effects = pulp.lpSum([x[k] for k in range(num_buttons) if j in q[i][k]])
            prob += effects == g[i][j], f"LED_{j}"
        prob += pulp.lpSum(x)
        # 求解 (使用默认 CBC 求解器，msg=0 关闭日志)
        status = prob.solve(pulp.PULP_CBC_CMD(msg=0))
        
        if pulp.LpStatus[status] == "Optimal":
            presses = sum(pulp.value(xi) for xi in x)
            res += presses
        else:
            raise ValueError("No optimal solution found for machine")
       
       


    print(res)

    


aoc_2()