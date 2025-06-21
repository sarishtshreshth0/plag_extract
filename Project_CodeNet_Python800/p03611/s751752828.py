N = int(input())
As = list(map(int,input().split()))
c = 0
nums = [0]*(10**5+2)
for a in As:
    nums[a]+=1

for i in range(1,len(nums)-1):
    t = nums[i-1]+nums[i]+nums[i+1]
    c = max(c,t)
print(c)


