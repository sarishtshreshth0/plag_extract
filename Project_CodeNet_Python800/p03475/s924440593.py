from math import ceil
n=int(input())
c=[0]*n
s=[0]*n
f=[0]*n
for i in range(n-1):
  c[i],s[i],f[i]=map(int,input().split())
for i in range(n):
  t=s[i]+c[i]
  if i<n-1:
    for j in range(i+1,n-1):
      if s[j]>=t:
        t=s[j]+c[j]
      else:
        t=ceil(t/f[j])*f[j]+c[j]
  print(t)