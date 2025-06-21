N,M = map(int,input().split())

X = list(map(int,input().split()))

X.sort()

memo = []

for i in range(1,M):
    memo.append(X[i]-X[i-1])

memo.sort()
#print(memo)
ans = 0
for i in range(M-N):
    ans += memo[i]
print(ans)