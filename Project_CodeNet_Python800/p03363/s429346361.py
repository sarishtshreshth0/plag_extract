N = int(input())
A = list(map(int,input().split()))
B = [0 for _ in range(N+1)]
for i in range(1,N+1):
    B[i] = B[i-1]+A[i-1]
C = {}
for i in range(N+1):
    b = B[i]
    if b not in C:
        C[b]=0
    C[b] += 1
cnt = 0
for b in C:
    n = C[b]
    if n>=2:
        cnt += (n*(n-1))//2
print(cnt)