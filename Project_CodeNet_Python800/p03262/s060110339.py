def gcd(a,b):
 while b!=0:
   a,b=b,a%b
 return a

n,x = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
tmp = abs(l[0]-x)

for i in range(1,n):
    tmp =  gcd(tmp,abs(l[i]-x))

print(tmp)