from collections import deque
n = int(input())
ki = [[] for i in range(n)]
lis = []
for i in range(n-1):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    ki[a].append(b)
    ki[b].append(a)
    lis.append([a,b,i])
mx = 0
for i in range(n):
    ki[i].sort()
    mx = max(mx,len(ki[i]))
lis = sorted(lis, key=lambda x:x[0])
lis = sorted(lis, key=lambda x:x[1])
lis2 = [[] for i in range(n)]
cnt = 0
for i in range(n-1):
    lis2[lis[i][0]].append(lis[i])
#print(lis2)

#print(ki)
def bfs(ki,lis2):
    d = [True] * n
    que = deque([(0,-1)])
    d[0] = False
    while len(que) != 0:
        val = que.popleft()
        cnt = 1
        cnt2 = 0
        for i in range(len(ki[val[0]])):
            if d[ki[val[0]][i]] == True:
                d[ki[val[0]][i]] = False

                #print(cnt,cnt2,val,i)
                if val[1] == cnt:
                    cnt += 1
                lis2[val[0]][cnt2].append(cnt)
                que.append([ki[val[0]][i],cnt])
                cnt += 1
                cnt2 += 1

    return lis2
lis2 = bfs(ki,lis2)
#print(lis2)
val = 0
for i in range(n):
    val = max(len(ki[i]),val)
print(val)
lis = []
for i in range(n):
    for j in range(len(lis2[i])):
        lis.append(lis2[i][j])
lis = sorted(lis,key=lambda x:x[2])
for i in range(n-1):
    print(lis[i][3])
