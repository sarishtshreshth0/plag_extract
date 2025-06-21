import sys
from fractions import gcd

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
A.sort()

# i番目を書き換えたgcdでは左からi-1番目までと、
# 右からi+1番目までのgcdのgcd

l = [0 for _ in range(N+1)]
tmp = 0
for i in range(N):
	tmp = gcd(tmp, A[i])
	l[i+1] = tmp

r = [0 for _ in range(N+1)]
A = A[::-1]
tmp = 0
for i in range(N):
	tmp = gcd(tmp, A[i])
	r[N-i-1] = tmp
 
m = [gcd(l[i], r[i+1]) for i in range(N)]
print(max(m))