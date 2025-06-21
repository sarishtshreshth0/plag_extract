from math import gcd
n = int(input())
l = list(map(int,input().split()))
mi = 1
gcd_l = [l[0]]
gcd_r = [l[-1]]
for i in range(1,n):
  gcd_l.append(gcd(l[i],gcd_l[-1]))
for i in range(n-2,-1,-1):
  gcd_r.append(gcd(l[i],gcd_r[-1]))
  
for i in range(0,n-2):
  t = gcd(gcd_l[i], gcd_r[n-3-i])
 # print(t)
  mi = max(mi,t)
#print(gcd_l)
#print(gcd_r)
mi = max(mi,gcd_r[-2])
mi = max(mi,gcd_l[-2])
print(mi)