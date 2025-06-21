from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

m,d=nii()

ans=0
for i in range(1,m+1):
  for j in range(1,d+1):
    if j>=10:
      d1=j%10
      j//=10
      d2=j
      if d1>=2 and d2>=2 and d1*d2==i:
        ans+=1

print(ans)