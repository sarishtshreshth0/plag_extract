n, m = map(int, input().split())
X = list(map(int, input().split()))
 
ans = 0
if n < m:
    X.sort()
    L = sorted([X[i + 1] - X[i] for i in range(m - 1)], reverse=True)
    ans = sum(L[n - 1: ])
 
print(ans)                
