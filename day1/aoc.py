import sys
sys.stdin = open('./day1/input.txt', 'r')
sys.stdout = open('./day1/output.txt', 'w')

def aoc_1():
    index = 50
    g = []
    try:
        while True:
            g.append(input())
    except EOFError:
        pass
    ans = 0
    for s in g:
        cnt = int(s[1:])
        if s[0] == 'L':
            index = (index - cnt +  100) % 100
        else:
            index = (index + cnt) % 100
        if index == 0:
            ans += 1
    print(ans)

def aoc_2():
    index = 50
    g = []
    try:
        while True:
            g.append(input())
    except EOFError:
        pass
    ans = 0
    for s in g:
        cnt = int(s[1:])
        ans += cnt // 100
        cnt %= 100

        if s[0] == 'L':
            if cnt > index  and index != 0:
                ans += 1
            index = (index - cnt +  100) % 100
        else:
            if cnt > 100 - index and index != 0:
                ans += 1
            index = (index + cnt) % 100
        if index == 0:
            ans += 1
    print(ans)

aoc_2()