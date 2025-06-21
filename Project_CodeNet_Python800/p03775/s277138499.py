from math import *
n=int(input())
l=[]
for i in range(1,int(sqrt(n))+1):
    if(n%i==0):
        l.append([i,n//i])
d=[]
for i in range(len(l)):
    x=str(l[i][0])
    y=str(l[i][1])
    d.append(max(len(x),len(y)))
print(min(d))
