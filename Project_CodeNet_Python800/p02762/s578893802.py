from collections import deque

n,m,k=map(int,input().split())
fre=[[]for _ in range(n)]
blo=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    fre[a-1].append(b-1)
    fre[b-1].append(a-1)
for i in range(k):
    c,d=map(int,input().split())
    blo[c-1].append(d-1)
    blo[d-1].append(c-1)

cnt=[0]*n
l=deque()
x=1
dic={}
for i in range(n):
    if cnt[i]==0:
        l.append(i)
    while l:
        now=l.popleft()
        for to in fre[now]:
            if cnt[to]==0:
                cnt[to]=x
                if x in dic:
                    dic[x]+=1
                else:
                    dic[x]=1
                l.append(to)
    x+=1

for i in range(n):
    if dic=={}:
        print(0)
    else:
        k=len(fre[i])
        for b in blo[i]:
            if cnt[b]==cnt[i]:
                k+=1
        if cnt[i] in dic:
            print(dic[cnt[i]]-k-1)
        else:
            print(0)