n=int(input())
w=[int(x) for x in input().split()]
r=sum(w)
l=0
ans=r
for i in range(n):
  l+=w[i]
  r-=w[i]
  ans=min(ans, abs(l-r))
print(ans)