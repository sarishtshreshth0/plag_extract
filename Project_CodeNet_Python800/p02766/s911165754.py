n,k=input().split()
n=int(n)
k=int(k)
count=0

while n>0:
  n=n//k
  count=count+1
  
print(count)