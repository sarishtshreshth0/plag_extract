n, m = map(int,input().split())
X = list(map(int,input().split()))
X.sort()

dist = []
for i in range(m-1):
    dist.append(X[i+1]-X[i])
dist.sort()
    
ans = 0
for i in range(max(m-n,0)):
    ans += dist[i]

print(ans)