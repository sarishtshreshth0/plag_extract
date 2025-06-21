mod = 998244353
n = int(input())
d = list(map(int,input().split()))
if d[0]!=0 or d[1:].count(0)!=0:
  print(0)
  exit()
l = [0 for i in range(n)]
for i in d:
  l[i] += 1
cou = 1
if 0 in l:
  a = l.index(0)
  if sum(l[a:])!=0:
    print(0)
    exit()
for i in range(n-2):
  if l[i+1]!=0:
    a = l[i]
    b = l[i+1]
    cou *= (a**b)%mod
print(cou%mod)