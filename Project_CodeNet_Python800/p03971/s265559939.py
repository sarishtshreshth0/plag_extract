from sys import stdin
from math import ceil, floor
n,a,b=[int(x) for x in stdin.readline().rstrip().split()]
s=list(stdin.readline().rstrip())
c=a+b
d=e=m=0
for i in range(n):
    if d<c and s[i]=="a":
        print("Yes")
        d+=1
    elif d<c and e<b and s[i]=="b":
        print("Yes")
        d+=1
        e+=1
    else:
        print("No")
    if d>=c:
        m=i+1
        break
if m != 0:
    for i in range(n-m):
        print("No")