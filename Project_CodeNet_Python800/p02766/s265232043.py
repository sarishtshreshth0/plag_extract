n,k=[int(s) for s in input().split()]

count=0
while n>0:
  n=n//k
  count=count+1
print(count)