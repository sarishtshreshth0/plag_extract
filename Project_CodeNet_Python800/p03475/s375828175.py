import math

N,*CSFf = map(int, open(0).read().split())
C = [x for x in CSFf[0::3]]
S = [x for x in CSFf[1::3]]
F = [x for x in CSFf[2::3]]
ans = [0] * N
for i in range(N-1):
    temp = S[i] + C[i]
    for j in range(i+1,N-1):
        if temp <= S[j]:
            temp = S[j] + C[j]
        else:
            temp = math.ceil(temp/F[j]) * F[j] + C[j]
    ans[i] = temp
for x in ans:
    print(x)