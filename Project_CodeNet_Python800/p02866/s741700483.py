N = int(input())
D = list(map(int, input().split()))
mod = 998244353
ans = 1
A = [0]*(max(D)+1)
for i in range(N):
  A[D[i]] += 1
if D[0] != 0 or not all(D[1:]) or not all(A):
  print(0)
  exit()
for i in range(1, max(D)+1):
  ans = ans * pow(A[i-1], A[i], mod) % mod
print(ans % mod)