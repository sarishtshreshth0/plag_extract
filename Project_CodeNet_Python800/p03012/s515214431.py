n=int(input())
w=[int(x) for x in input().rstrip().split()]
SUM=sum(w)

now=0
ans=float('inf')
for i in w:
  now+=i
  ans=min(abs(now-(SUM-now)),ans)
print(ans)
