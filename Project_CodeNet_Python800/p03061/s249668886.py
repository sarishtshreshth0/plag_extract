import math
N = int(input())
num = list(map(int, input().split()))

gL = [0]*(N+2)
gR = [0]*(N+2)

def gdc(a, b):
    if a < b: a, b = b, a
    if b == 0: return a

    while (a > b) and (a % b > 0):
        a = a - b
        if a < b:
            a, b = b, a

    return b

gL[0] = 0
gR[N] = 0
for i in range(1, N+1):
    gL[i] = gdc(gL[i-1], num[i-1])

for i in range(N-2, -1, -1):
    gR[i] = gdc(gR[i+1], num[i+1])

ans = 0
for i in range(0, N):
    gg = gdc(gL[i], gR[i])
    if ans < gg:
        ans = gg

print(ans)

