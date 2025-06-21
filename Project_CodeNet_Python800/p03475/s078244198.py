import sys
input = sys.stdin.readline

n = int(input())
C = []
S = []
F = []
for _ in range(n-1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)

for i in range(n-1):
    t = 0
    for j in range(i, n-1):
        c = C[j]
        s = S[j]
        f = F[j]

        t = max(t, s)
        if t % f:
            t += f - (t % f)
        t += c
    print(t)
print(0)