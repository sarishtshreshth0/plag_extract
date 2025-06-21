inp=list(map(int,input().split()))
n=inp[0]
arr=[]
for i in range(n):
  inp=list(map(int,input().split()))
  arr.append(inp)
ans=0
for i in range(len(arr)):
  for j in range(i+1,len(arr)):
    x=0
    for k in range(len(arr[0])):
      x+=(arr[i][k]-arr[j][k])**2
    z=int(pow(x,0.5))
    if z**2==x:
      ans+=1
print (ans)