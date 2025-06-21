a, b, c = map(int, input().split())
print("Yes" if max(a, b, c) != c and min(a, b, c) != c else "No")