import sys

sys.setrecursionlimit(4100000)
n = int(input())
numlist = [3, 5, 7]


ans = 0


def dfs(num, a, b, c):
    global ans
    if num > n:
        return False
    if a == 1 and b == 1 and c == 1:
        if num <= n:
            ans += 1
    for d in numlist:
        na, nb, nc = a, b, c
        if d == 3:
            na = 1
        if d == 5:
            nb = 1
        if d == 7:
            nc = 1
        if num == 0:
            num = d
        else:
            num = num * 10 + d
        dfs(num, na, nb, nc)
        num //= 10


dfs(0, 0, 0, 0)
print(ans)
