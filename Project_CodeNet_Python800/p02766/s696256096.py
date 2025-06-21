n,k=map(int,input().split())
ans=""
while n>0:
  ans+=str(n%k)
  n//=k
print(len(ans[::-1]))

