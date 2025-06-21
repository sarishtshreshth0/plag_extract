a, b, c, d = map(int, input().split())
ans = 0 if (b <= c) or (d <= a) else min(b, d) - max(a, c)
print(ans)
