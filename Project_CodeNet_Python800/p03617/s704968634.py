q,h,s,d=map(int,input().split())
n=int(input())
if 2*q<h:
  h=2*q
if 2*h<s:
  s=2*h
if 2*s<d:
  d=2*s
print(n//2*d+n%2*s)