from collections import deque
n , m , k = map(int,input().split())
tomo = [set() for i in range(n+1)]
to = [0 for i in range(n+1)]
bro = [set() for i in range(n+1)]
for i in range(m):
    a , b = map(int,input().split())
    tomo[a].add(b)
    tomo[b].add(a)
    to[a] += 1
    to[b] += 1
for i in range(k):
    c , d = map(int,input().split())
    bro[c].add(d)
    bro[d].add(c)

visit = [True for i in range(n+1)]
kurasuta = []
for i in range(1,n+1):
    if visit[i]:
        kar = {i}
        d = deque()
        d.append(i)
        cou = 1
        visit[i] = False
        while d:
            now = d.popleft()
            for j in tomo[now]:
                if visit[j]:
                    visit[j] = False
                    kar.add(j)
                    d.append(j)
                    cou += 1
        kurasuta.append([kar,cou])
    else:
        continue
ans = [0 for i in range(n)]

for i in range(len(kurasuta)):
    for j in kurasuta[i][0]:
        ans[j-1] = len(kurasuta[i][0]) - to[j] - 1 - len(kurasuta[i][0] & bro[j])

print(*ans)
