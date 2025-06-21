n=int(input())
lst=list(map(int,input().split()))
dist=[[] for _ in range(n)]
for i in range(n):
    dist[lst[i]].append(i)
if len(dist[0])!=1:
    print(0)
    exit()
if not 0 in dist[0]:
    print(0)
    exit()

switch=0
for i in range(-1,-n-1,-1):
    if switch==0:
        if len(dist[i])>=1:
            switch=1
    if switch==1:
        if len(dist[i])==0:
            print(0)
            exit()
ans=1
rem=1
for i in range(n):
    num=len(dist[i])
    ans*=pow(rem,num,998244353)
    ans%=998244353
    rem=num
print(ans)