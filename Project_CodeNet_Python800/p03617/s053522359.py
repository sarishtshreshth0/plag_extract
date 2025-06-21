q,h,s,d=map(int,input().split())
n=int(input())
h=min(2*q,h)
s=min(2*h,s)
d=min(2*s,d)
ans=0
data=[[2,d],[1,s],[float(0.5),h],[float(0.25),q]]
for i in range(4):
  ans+=(int(n/data[i][0]))*data[i][1]
  n-=(int(n/data[i][0]))*data[i][0]
print(int(ans))