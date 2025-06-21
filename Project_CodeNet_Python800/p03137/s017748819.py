N, M = list(map(int,input().split()))
X = list(map(int,input().split()))
X = sorted(X)
diff = []
for i in range(M - 1):
    diff.append(abs(X[i] - X[i + 1]))
    
diff = sorted(diff)[::-1]
ans = sum(diff[N - 1:])
print(ans)