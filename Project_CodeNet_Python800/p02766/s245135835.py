n,k=map(int,input().split())
a,b=0,0
for i in range(1000000000):
  if n//k ==0:
    break
  else:
    n=n//k
    a+=1
print(a+1)