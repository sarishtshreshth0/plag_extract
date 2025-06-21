from collections import deque

n,m,k = map(int,input().split())

cango = [[]for i in range(n)]
cannotgo=[[]for i in range(n)]
for i in range(m):
    a,b = (map(int,input().split()))
    a,b = a-1,b-1
    cango[a].append(b)
    cango[b].append(a)

for i in range(k):
    c,d =(map(int,input().split()))
    c,d = c-1,d-1
    cannotgo[c].append(d)
    cannotgo[d].append(c)
# print(a)
# cango = [[]for i in range(n)]
# for i in a:
#     cango[i[0]-1].append(i[1]-1)
#     cango[i[1]-1].append(i[0]-1)
# print(cango)

# cannotgo=[[]for i in range(n)]
# for i in c:
#     cannotgo[i[0]-1].append(i[1]-1)
#     cannotgo[i[1]-1].append(i[0]-1)
# # print(cannotgo)
alre = [False]*n
parent = [-1]*n
gro = {}
y = deque()
# print(gro)
for i in range(n):
    # if alre[i]==True:
    #     continue
    # gro[i]=set([i])
    y.append(i)
    leader = i
    cnt = 0 
    while len(y)>0:
        x = y.popleft()
        if parent[x]!=-1:
            continue
            # print(to)
        parent[x]=leader
        y.extend(cango[x])
        cnt +=1
    if cnt!=0:
        gro[leader]=cnt
# print(gro)
# print(parent)
ans = [0]*n
# print(ans)
for iam in range(n):
    # group = gro[parent[iam]]
    tmp_ans = gro[parent[iam]]
    tmp_ans -=1
    tmp_ans -= len(cango[iam])
    for block in cannotgo[iam]:
        if parent[block]==parent[iam] :
            tmp_ans -=1
    ans[iam]=tmp_ans
print(*ans, sep=' ')