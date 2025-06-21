a, b, c, d = map(int, input().split())
print(0) if b <= c or d <= a else print(min(d-a, b-c, b-a, d-c))