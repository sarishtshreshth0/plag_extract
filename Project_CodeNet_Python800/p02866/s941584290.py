def pow_r(x,n,p):
  if n == 0:
    return 1
  if n % 2 == 0:
    return pow_r(x**2 % p, n//2, p)
  else:
    return x * pow_r(x**2 % p, n//2, p) % p
    

N = int(input())
Ds = list(map(int, input().split()))
memo = [0]*N
P = 998244353

for d in Ds:
  memo[d] += 1
  
if Ds[0] != 0 or memo[0] != 1:
  print(0)
  exit()
  
rlt = 1
cnt = 1

for i in range(1,N):
  if memo[i] > 0:
    rlt *= pow_r(memo[i-1], memo[i], P)
    rlt %= P
    cnt += memo[i]
  else:
    if cnt == N:
      print(rlt)
      exit()
    else:
      print(0)
      exit()
      
print(rlt)
