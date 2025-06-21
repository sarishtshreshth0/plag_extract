M,D=map(int,input().split())
cnt = 0
for i in range(11,D+1):
  d10=i//10
  d1=i%10
  if d1*d10 <= M and d10>=2 and d1>=2:
    cnt+=1
print(cnt)