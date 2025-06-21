n=int(input())
b=[0 for i in range(100002)]
a=list(map(int,input().split()))
a.sort()
for i in range(n):
    b[a[i]]+=1
ans=0
for i in range(1,100001):
    tmp=b[i-1]+b[i]+b[i+1]
    if tmp>ans:
        ans=tmp
print(ans)