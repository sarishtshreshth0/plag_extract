from collections import deque
n,m,k=map(int,input().split())

F=[set() for i in range(n)]
B=[set() for i in range(n)]
for i in range(m):
	a,b=map(int,input().split())
	a,b=a-1,b-1
	F[a].add(b)
	F[b].add(a)
for i in range(k):
	c,d=map(int,input().split())
	c,d=c-1,d-1
	B[c].add(d)
	B[d].add(c)
	
T=[set() for i in range(n)]
D=[0]*n
R=[0]*n

for i in range(n):
    if D[i]:
        continue
    que=deque([])
    que.append(i)
    S=set()
    S.add(i)
    while que:
        p=que.popleft()
        for np in F[p]:
            if D[np]!=1:
                que.append(np)
                S.add(np)
                D[np]=1
    for s in S:
        R[s]=len(S)-len(F[s])-len(S&B[s])-1

print(*R)