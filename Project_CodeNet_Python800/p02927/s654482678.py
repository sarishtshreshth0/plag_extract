M,D=map(int,input().split())

ans=0
for i in range(22,D+1):
  if min(divmod(i,10)) in (0,1):
    continue
  q,r=divmod(i,10)
  if q*r <= M:
    ans += 1

print(ans)