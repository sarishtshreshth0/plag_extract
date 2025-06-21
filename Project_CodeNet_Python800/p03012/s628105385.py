n=int(input())
w=list(map(int,input().split()))
s=[0]*n
for i in range(n-1):
  s[i+1]=s[i]+w[i]
ans=sum(w)
for i in range(1,n):
  ans=min(ans,abs((sum(w)-s[i])-s[i]))
print(ans)