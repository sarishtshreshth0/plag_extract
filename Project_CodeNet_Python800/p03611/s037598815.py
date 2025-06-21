N = int(input())
A = list(map(int,input().split()))
C = {i:0 for i in range(0,10**5)}
for i in range(N):
    C[A[i]] += 1
cmax = 0
for x in range(1,10**5-1):
    cnt = C[x]+C[x-1]+C[x+1]
    cmax = max(cmax,cnt)
print(cmax)