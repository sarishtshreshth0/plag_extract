A, B, C, D = map(int, input().split())
t = min(B, D) - max(A, C)
print(t if t > 0 else 0)