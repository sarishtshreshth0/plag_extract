A, B, C = list(map(int, input().split()))
print("Yes" if (C < A) ^ (C < B) else "No")
