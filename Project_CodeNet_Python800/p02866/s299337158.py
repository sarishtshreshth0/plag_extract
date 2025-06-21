n=int(input())
d=list(map(int,input().split()))
mx=max(d)
l=[0]*(10**5)
mx=0
for i in range(n):
    if (i==0 and d[i]!=0) or (i!=0 and d[i]==0):
        print(0)
        exit()
    l[d[i]]+=1
    mx=max(mx,d[i])
t=1
ans=1
for i in range(1,mx+1):
    ans *= t**l[i]
    t=l[i]

print(ans%998244353)