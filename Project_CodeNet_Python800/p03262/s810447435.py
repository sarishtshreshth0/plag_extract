import math
n,p=map(int,input().split())
a=list(map(int,input().split()))
x=[]
for i in a:
  x.append(abs(i-p))
  
if len(x)==1:
  print(x[0])
  
else:
  pin=x[0]
  for i in range(1,len(x)):
    pin=math.gcd(pin,x[i])
    
  print(pin)