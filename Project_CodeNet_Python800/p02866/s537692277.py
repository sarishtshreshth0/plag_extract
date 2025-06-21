n = int(input())
d = list(map(int ,input().split()))
if d[0] != 0:
  print (0)
  exit()
d.sort()
mod = 998244353
s = [0 for i in range(max(d)+1)]

for i in range(n):
  s[d[i]] += 1
ans = 1
for i in range(len(s)):
  if s[i] == 0:
    print (0)
    exit()
  if i == 0:
    if s[i] > 1:
      print (0)
      exit()
    continue
  ans *= pow(s[i-1],(s[i]),mod)
  ans %= mod
print (ans%mod)