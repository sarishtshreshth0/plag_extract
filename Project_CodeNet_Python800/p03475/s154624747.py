import sys
n, *CSF = list(map(int, sys.stdin.buffer.read().split()))
C = CSF[::3]
S = CSF[1::3]
F = CSF[2::3]


def solve(x):
    cur = 0
    for i in range(x, n - 1):
        y = cur % F[i]
        if S[i] > cur:
            cur = S[i] + C[i]
        elif y == 0:
            cur += C[i]
        else:
            cur += (F[i] - y) + C[i]
    return cur


for i in range(n - 1):
    print(solve(i))
print(0)
