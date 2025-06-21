import math
n=int(input())
l=math.floor(math.sqrt(n))
k=math.floor(math.log10(n))+1

for i in range(2,l+1):
    if n%i==0:
        a,b=i,n//i
        x=max(math.floor(math.log10(a))+1,math.floor(math.log10(b))+1)
        k=min(x,k)
print(k)