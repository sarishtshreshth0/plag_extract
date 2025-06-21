N=int(input())
a=list(map(int,input().split()))

nums=[0]*(10**5+1)
for i in a:
    nums[i]+=1

ans0=nums[0]+nums[1]+nums[2]
ans=ans0
for i in range(2,10**5-1):
    ans1=ans0-nums[i-2]+nums[i+1]
    ans=max(ans,ans1)
    ans0=ans1

print(ans)