n=int(input())
a=list(map(int,input().split()))
am=max(a)
num=[0]*(am+1)
for i in a:
  num[i]+=1
#print(num)
mx=0
for i in range(1,am):
  #print(num[i-1:i+2])
  m=sum(num[i-1:i+2])
  if m>mx:
    mx=m
if len(num)<=3:
  mx=sum(num)
print(mx)