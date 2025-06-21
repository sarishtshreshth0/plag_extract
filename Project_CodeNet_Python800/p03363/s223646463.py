n=int(input())
a=list(map(int,input().split()))
dic={}
current=0
dic[0]=1
for i in range(n):
  current+=a[i]
  if current in dic:
    dic[current]+=1
  else:
    dic[current]=1
ans=0
for i in dic:
  ans+=(dic[i]*(dic[i]-1))//2
print(ans)