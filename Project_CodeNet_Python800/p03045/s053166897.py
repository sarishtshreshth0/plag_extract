from collections import defaultdict, deque
dic = defaultdict(list)

N, M = map(int, input().split())
hint= [-1]*N

for _ in range(M):
    x, y, z = map(int, input().split())
    dic[x].append(y)
    dic[y].append(x)
    hint[x-1]=0
    hint[y-1]=0
    
count = 0
ans=0
for i in range(N):
    if hint[i]==0:
        count+=1
        hint[i]=count
        queue = deque()
        for j in dic[i+1]:
            if hint[j-1]==0:
                queue.append(j)
                hint[j-1]=count
        while queue:
            x = queue.popleft()
            for k in dic[x]:
                if hint[k-1]==0:
                    hint[k-1]=count
                    queue.append(k)        
        continue
    elif hint[i]==-1:
        ans+=1
print(ans+count)
