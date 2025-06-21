N = int(input())
A = list(map(int,input().split()))

B = {}
for i in range(N):
    for j in [-1,0,1]:
        if A[i] + j in B:
            B[A[i]+j] += 1
        else:
            B[A[i]+j] = 1
print(max(B.values()))