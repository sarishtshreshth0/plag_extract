import math
N = int(input())
CSF = []
for _ in range(N-1):
    c, s, f = map(int, input().split())
    CSF.append((c, s, f))

ans = []
for i in range(N):
    T = 0
    for j in range(i, N-1):
        T = max(CSF[j][1], math.ceil(T/CSF[j][2])*CSF[j][2])
        T += CSF[j][0]
    ans.append(T)


print(*ans, sep='\n')
