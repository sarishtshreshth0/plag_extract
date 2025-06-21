N, M = map(int, input().split())
X = list(map(int, input().split()))
X = sorted(X)
diff = []

# 地点間の距離をdiffに記憶
for i in range(M - 1):
    diff.append(abs(X[i] - X[i + 1]))

# N個の区間でM個の地点を覆う
# すると、N-1個の覆われていない区間ができる
# これを最大にすると覆う区間を最小にできる

diff = sorted(diff, reverse=True)
#print(diff)
# diffの中で大きい順にN-1個の総和をとる
#数直線の長さ - 覆わなくて良い範囲の総和
ans = (X[-1] - X[0]) - sum(diff[:N - 1])
# ans = sum(diff[:N-1]) でもOK、どうしても覆う必要がある区間の和
print(ans)
