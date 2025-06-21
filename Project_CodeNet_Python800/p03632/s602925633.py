a, b, c, d = map(int, input().split())
ans = (min([b, d]) - max([a, c])) if (min([b, d]) - max([a, c])) > 0 else 0
print(ans)