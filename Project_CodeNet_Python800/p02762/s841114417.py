from collections import deque
#空のリスト 作った後は普通にappend使えばOK
n,m,k=map(int,input().split())
 
tomodati=[[] for i in range(n+1)]
 
group=[0]*(n+1)

group_cnt=[0]*(n+1)
 
block=[0]*(n+1)
 
tansaku=deque()
 
for i in range(m):
    a,b=map(int,input().split())
    tomodati[a].append(b)
    tomodati[b].append(a)
 
num=1
 
for i in range(1,n+1):
    if group[i]==0:
        tansaku.append(i)
        group[i]=num
        group_cnt[num]+=1
    else:
        continue
    while len(tansaku)>0:
        for j in tomodati[tansaku[0]]:
            if group[j]==0:
                group[j]=num
                group_cnt[num]+=1
                tansaku.append(j)
        tansaku.popleft()
    num+=1
 
for i in range(k):
    c,d=map(int,input().split())
    if group[c]==group[d]:
        block[c]+=1
        block[d]+=1
 
ans=[]
 
for i in range(1,n+1):
    ans.append(group_cnt[group[i]]-len(tomodati[i])-block[i]-1)
 
print(*ans)