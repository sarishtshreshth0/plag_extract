N, M = map(int, input().split())
X = list(map(int, input().split()))
ans = 0
if N >= M:
    ans = 0
    print(ans)
else:
    X.sort()
    diff = [X[i+1] - X[i] for i in range(M-1)]
    diff.sort()
    for j in range(M-N):
        ans += diff[j]
    print(ans)