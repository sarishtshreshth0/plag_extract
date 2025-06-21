N=int(input())
L=[0]*(10**5+1)
A=list(map(int,input().split()))
A.sort()
for i in A:
  L[i]+=1
ans=0
for i in range(10**5-1):
  ans=max(ans,L[i]+L[i+1]+L[i+2])
print(ans)