n=int(input())
a=list(map(int,input().split()))
x=[0]*10**5
for i in a:
  x[i]+=1
ans=0
for i in range(10**5-2):
  ans=max(ans,x[i]+x[i+1]+x[i+2])
print(ans)