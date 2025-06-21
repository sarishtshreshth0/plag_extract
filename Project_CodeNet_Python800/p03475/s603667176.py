n=int(input())
csf=[list(map(int,input().split())) for _ in range(n-1)]
ans=[float("inf") for _ in range(n)]
ans[n-1]=0
for i in range(n-1):
  cnt=csf[i][1]+csf[i][0]
  for j in range(i+1,n-1):
    if csf[j][2]<cnt:
      if cnt%csf[j][2]==0:
        cnt+=csf[j][0]
      else:
        cnt+=csf[j][0]+csf[j][2]-cnt%csf[j][2]
    else:
      cnt+=cnt-csf[j][2]
  ans[i]=cnt
ans=ans[::-1]
ans.append(float("inf"))
for i in range(n):
  if ans[i]>ans[i+1]:
    ans[i+1]=ans[i]
ans.pop(-1)
for i in ans[::-1]:
  print(i)