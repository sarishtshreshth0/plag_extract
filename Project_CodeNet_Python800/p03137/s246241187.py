k, n = list(map(int, input().split()))
x = list(map(int, input().split()))
x.sort()
df = [0] * (n - 1)
for i in range(n - 1):
    df[i] = abs(x[i + 1] - x[i])

df = sorted(df, reverse=True)
print(sum(df[k - 1 :]))
