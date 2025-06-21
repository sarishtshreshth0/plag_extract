from collections import Counter
N = int(input())
A = list(map(int, input().split()))
for i in range (1, N):
  A[i] += A[i-1]
A = Counter(A)
k = 0
for j in A.values():
  k += j*(j-1)//2
k += A.get(0,0)
print(k)