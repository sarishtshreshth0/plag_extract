from collections import deque
N, M, K = map(int,input().split())
friendlist = [[] for _ in range(N+1)]
for n in range(M):
    A, B = map(int,input().split())
    friendlist[A].append(B)
    friendlist[B].append(A)

blocklist = [[] for _ in range(N+1)]
for n in range(K):
    C, D = map(int, input().split())
    blocklist[C].append(D)
    blocklist[D].append(C)

whatgroup = [-1 for _ in range(N+1)]
visited = [-1] * (N+1)
d = deque()
leaderdic = {}
for person in range(1,N+1):
    d.append(person)
    leader = person
    cnt = 0
    while len(d)>0:
        nowwho = d.popleft()
        if whatgroup[nowwho] != -1:
            continue
        d.extend(friendlist[nowwho])
        whatgroup[nowwho] = leader
        cnt += 1
    if cnt != 0:
        leaderdic[leader] = cnt
for person in range(1,N+1):
    ans = leaderdic[whatgroup[person]]
    ans -= 1
    ans -= len(friendlist[person])
    for block in blocklist[person]:
        if whatgroup[person]==whatgroup[block]:
            ans -= 1
    print(ans)