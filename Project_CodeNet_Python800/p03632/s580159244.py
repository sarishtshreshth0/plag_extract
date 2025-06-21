a, b, c, d = map(int, input().split())
start = max(a, c)
end = min(b, d)
ans = end - start if start <= end else 0
print(ans)