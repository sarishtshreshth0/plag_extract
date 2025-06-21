n, m = map(int, input().split())
x = sorted(map(int, input().split()))
y = sorted([x[i] - x[i - 1] for i in range(1, m)],reverse=True)
ans = x[-1] - x[0]
ans -= sum(y[:n-1])
print(ans)