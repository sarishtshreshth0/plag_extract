N=int(input())
arr=list(map(int,input().split()))

ans=1000

for i in range(1,N):
    temp=abs(sum(arr[0:i])-sum(arr[i:]))
    ans=min(ans,temp)

print(ans)