N = int(input())
A = [[0]*2 for _ in range(N)]
C = [[0]*2 for _ in range(N)]
for i in range(N):
    A[i][0],A[i][1] = map(int,(input().split()))
for i in range(N):
    C[i][0],C[i][1] = map(int,(input().split()))
    
C.sort()
ans = 0
for i in range(N):
    nim = 100000
    for j in range(len(A)):
        if A[j][0] < C[i][0]:
            tmp = C[i][1] - A[j][1]
            if 0 < tmp < nim:
                nim = tmp
                sa = j
    if nim != 100000:
        del A[sa]
        ans += 1

print(ans)