N, M = map(int, input().split())
X = list(map(int, input().split()))

if M <= N:
    print(0)
    exit()


X.sort()
diff = []
sum_dist = X[-1] - X[0]

for i, x in enumerate(X):
    diff.append(x - X[i - 1])


diff.sort(reverse=True)
print(sum_dist - sum(diff[:N - 1]))
