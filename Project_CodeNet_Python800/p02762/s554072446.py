from collections import defaultdict, deque
n, m, k = map(int, input().split())
friends = defaultdict(set)
block = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].add(b)
    friends[b].add(a)
for _ in range(k):
    c, d = map(int, input().split())
    block[c].add(d)
    block[d].add(c)
#print(friends)
#print(block)

roopname = []
roop = defaultdict(set)
seen = [0]*n


for i in range(n):
    if not seen[i]==0:
        continue
    seen[i] = i+1
    roopname.append(i+1)
    roop[i+1].add(i+1)
    queue = deque(friends[i+1])
    while queue:
        p = queue.popleft()
        if  not seen[p-1]==0:continue
        seen[p-1] = i+1
        roop[i+1].add(p)
        for j in friends[p]:
            if seen[j-1]==0:
                queue.append(j)
#print(roopname)
#print(roop)
#print(seen)
ans = [len(roop[seen[i]])-len(roop[seen[i]]&friends[i+1])-len(roop[seen[i]]&block[i+1])-1 for i in range(n)]

    

L=[str(a) for a in ans]
L=" ".join(L)
print(L)