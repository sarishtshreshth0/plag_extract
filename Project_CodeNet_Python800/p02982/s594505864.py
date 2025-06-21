n,d=map(int,input().split())
x=[]
cnt=0
for i in range(n):
  tmp=list(map(int,input().split()))
  x.append(tmp)
for i in range(n-1):
  for j in range(i+1,n):
    tmp=0
    for k in range(d):
      tmp+=(abs(x[i][k]-x[j][k]))**2
    if tmp**0.5==int(tmp**0.5):
      cnt+=1
print(cnt)