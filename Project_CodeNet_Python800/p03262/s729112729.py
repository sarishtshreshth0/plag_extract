N, X = map(int, input().split())
X_list = list(map(int, input().split()))
kyori = [abs(X - x) for x in X_list]


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


ans = kyori[0]
for i in range(1, N):
    ans = gcd(ans, kyori[i])
print(ans)
