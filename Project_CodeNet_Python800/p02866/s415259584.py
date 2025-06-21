n=int(input())
d=list(map(int,input().split()))
num=[0]*n
num[0]=1
if d[0]!=0 or d.count(0)!=1:
    print(0)
else:
    ans=1
    for i in range(1,n):
        num[d[i]]+=1
    for i in range(1,max(d)+1):
        ans*=num[i-1]**num[i]
        ans%=998244353
    print(ans)
