a,b,c,d=map(int,input().split())
lower=max(a,c)
upper=min(b,d)
ans=upper - lower
if ans<0:
  ans=0
print(ans)