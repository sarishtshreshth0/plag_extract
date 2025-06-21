n = int(input())
D = list(map(int, input().split()))

if D[0] != 0:
    print(0)
    exit()

A = [0]*n

for i in range(n):
    A[D[i]] += 1

#print(A)

if A[0] != 1:
    print(0)
    exit()

ans = 1
mod = 998244353
for i in range(1, n):
    ans *= A[i-1]**A[i]
    ans %= mod
print(ans)
