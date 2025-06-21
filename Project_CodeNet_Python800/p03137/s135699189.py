N,M = map(int,input().split())
X = list(map(int, input().split()))
X.sort()
diss=[0]*(M-1)
allDistance = abs(X[0])
for i in range(1,M):
    allDistance += X[i]
    diss[i-1] = abs(X[i]-X[i-1])
diss.sort(reverse=True)
print(sum(diss[N-1:]))