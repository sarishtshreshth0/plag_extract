p=998244353
n=int(input())
d=list(map(int,input().split()))
dep = [0]*n
for x in d:
  dep[x] += 1

ans = 1 if d[0]==0 and dep[0]==1 else 0
for i in range(1,n):
  ans *= (dep[i-1]%p) ** dep[i] % p
  ans %= p

print(ans)