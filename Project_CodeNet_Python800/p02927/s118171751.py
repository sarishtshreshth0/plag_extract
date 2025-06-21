M,D=map(int,input().split())
ans=0
for i in range(11,D+1):
  a,b=0,0
  if i%10>=2:
    a=i%10
  if i//10>=2:
    b=i//10
  if 4<=a*b<=M:
    ans+=1
print(ans)
