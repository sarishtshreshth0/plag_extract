n=int(input())
a=list(map(int,input().split()))
lis=[0]*100001
for num in a:
    lis[num]+=1
ans=0
for i in range(100001-2):
    ans=max(ans,lis[i]+lis[i+1]+lis[i+2])
print(ans)