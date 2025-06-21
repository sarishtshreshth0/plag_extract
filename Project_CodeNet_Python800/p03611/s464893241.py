N = int(input())
A = list(map(int,input().split()))
L = [0]*(10**5+10)
for i in range(N):
    L[A[i]] += 1
    L[A[i]+1] += 1
    L[A[i]+2] += 1
print(max(L))
