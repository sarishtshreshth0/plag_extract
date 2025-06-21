N = int(input())
weight = list(map(int, input().strip().split()))
 
S1 = 0
S2 = 0
 
for i in range(N):
    S1 += weight[i]
 
res = S1
for i in range(N):
    S1 -= weight[i]
    S2 += weight[i]
    if S1 < S2:
        if S2 - S1 < res:
            res = S2 - S1
        break
    if S1 - S2 < res:
        res = S1 - S2
 
print(res)