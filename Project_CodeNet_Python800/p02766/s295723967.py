n,k=map(int,input().split())

count=1
subk=k

while subk<=n:
  subk*=k
  count+=1
  
print(count)