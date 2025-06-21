A, B, C = list(map(int, input().split()))
print("Yes" if (A-C) * (C-B) > 0 else "No")