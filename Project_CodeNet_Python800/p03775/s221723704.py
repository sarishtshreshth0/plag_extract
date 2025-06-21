from math import sqrt,ceil
n=int(input())
a=ceil(sqrt(n))
l=[]
p=[]
for i in range(1,a+1):
    if n%i==0:
        l.append([i,n//i])
        x=len(str(i))
        y=len(str(n//i))
        p.append(max(x,y))

print(min(p))
