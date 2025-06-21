import sys

stdin = sys.stdin
inf = 1 << 60
mod = 1000000007

sys.setrecursionlimit(10 ** 7)

ni      = lambda: int(ns())
nin     = lambda y: [ni() for _ in range(y)]
na      = lambda: list(map(int, stdin.readline().split()))
nan     = lambda y: [na() for _ in range(y)]
nf      = lambda: float(ns())
nfn     = lambda y: [nf() for _ in range(y)]
nfa     = lambda: list(map(float, stdin.readline().split()))
nfan    = lambda y: [nfa() for _ in range(y)]
ns      = lambda: stdin.readline().rstrip()
nsn     = lambda y: [ns() for _ in range(y)]
ncl     = lambda y: [list(ns()) for _ in range(y)]
nas     = lambda: stdin.readline().split()

from collections import deque

n = ni()
s = ns()

q = deque()
for i in range(n):
    p = q.pop() if len(q) else '$'
    if not (p == '(' and s[i] == ')'):
        if p != '$':
            q.append(p)
        q.append(s[i])

ans = deque(s)
for c in q:
    if c == ')':
        ans.appendleft('(')
    else:
        ans.append(')')

print(*ans, sep="")