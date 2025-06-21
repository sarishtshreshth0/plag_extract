N,M = map(int,input().split())
X = list(map(int,input().split()))
X.sort()
index = []
ans = 0
s = 0
for i in range(len(X)-1):
    index.append([i,X[i+1]-X[i]])
index.sort(key=lambda x: x[1],reverse=True)
if N<M:
    for i in range(N-1,len(index)):
        ans += index[i][1]

print(ans)

