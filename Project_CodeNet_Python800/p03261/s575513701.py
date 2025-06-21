from collections import *
n=int(input())
l=[]
for i in range(n):
    l.append(input())
f=0
c=Counter(l)
for i in c.values():
    if(i>1):
        f=1
        break
if(f==1):
    print("No")
else:
    d=0
    for i in range(1,n):
        if(l[i-1][-1]!=l[i][0]):
            d=1
            break
    if(d==1):
        print("No")
    else:
        print("Yes")
