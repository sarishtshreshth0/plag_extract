n=int(input())
inf=float('inf')
ans=inf
for i in range(1,10**5+1):
  if n%i==0:
    q=n//i
    s=max(len(str(i)),len(str(q)))
    ans=min(ans,s)
    
print(ans)