n = int(input())
mod = 998244353
count = [0]*(10**5+1)
L = list(map(int,input().split()))
M = max(L)
ans = 0
for i in range(n):
  count[L[i]] += 1
for i in range(M+1):
  if count[i] == 0:
    ans = 0
    break
  else:
    if i == 0:
      if count[i] != 1:
        ans = 0
        break
      else:
        ans = 1
    else:
      ans = ans*((count[i-1]**count[i])%mod)
      ans = ans%mod
if L[0] == 0:
  print(ans)
else:
  print(0)