n=int(input())
i=1
ans=1
while i*i<=n:
  if n%i==0:
    ans=i
  i+=1
print(len(str(n//ans)))