n, m = map(int, input().split())
X = list(map(int, input().split()))
X.sort()

if n >= m:
    print(0)
    exit()

sa = []

for i in range(1, m):
    sa.append(abs(X[i] - X[i - 1]))

sa.sort(reverse=True)
# print(sa)
# print((max(X) - min(X)))
print((max(X) - min(X)) - sum(sa[:n-1]))
