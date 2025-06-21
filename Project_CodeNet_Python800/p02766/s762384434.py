n,k=[int(s) for s in input().split()]

r=[]
i=0
a=0
while n>0:
  i=n%k
  n=n-i
  n=n//k
  r.append(i)
  a=a+1
  

print(a)