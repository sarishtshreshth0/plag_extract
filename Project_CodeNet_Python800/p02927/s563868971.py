import sys

stdin = sys.stdin
inf = 1 << 60
mod = 1000000007

sys.setrecursionlimit(10**7)

ni = lambda: int(ns())
nin = lambda y: [ni() for _ in range(y)]
na = lambda: list(map(int, stdin.readline().split()))
nan = lambda y: [na() for _ in range(y)]
nf = lambda: float(ns())
nfn = lambda y: [nf() for _ in range(y)]
nfa = lambda: list(map(float, stdin.readline().split()))
nfan = lambda y: [nfa() for _ in range(y)]
ns = lambda: stdin.readline().rstrip()
nsn = lambda y: [ns() for _ in range(y)]
ncl = lambda y: [list(ns()) for _ in range(y)]
nas = lambda: stdin.readline().split()

m, d = na()

cur_m = 1
cur_d = 1
ans = 0
while cur_m // (m + 1) != 1:
    while cur_d // (d + 1) != 1:
        if cur_d % 10 >= 2 and cur_d // 10 >= 2:
            ans += ((cur_d % 10) * (cur_d // 10)) == cur_m
        cur_d += 1
    cur_d = 1
    cur_m += 1

print(ans)