N = int(input())
A = list(map(int,input().split()))
C = {}
for i in range(N):
    if A[i] not in C:
        C[A[i]] = 0
    C[A[i]] += 1
cmax = 0
for a in A:
    cnt = C[a]
    if a-1 in C:
        cnt += C[a-1]
    if a+1 in C:
        cnt += C[a+1]
    cmax = max(cmax,cnt)
print(cmax)