M,D=map(int,input().split())

cnt=0
for m in range(1,M+1):
  for d in range(1,D+1):
    s=d//10
    t=d%10
    if s>=2 and t>=2 and s*t==m:
      cnt +=1
print(cnt)