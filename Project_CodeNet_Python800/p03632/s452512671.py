A, B, C, D = map(int, input().split())

minv = max(A, C)
maxv = min(B, D)

print(max(0, maxv - minv))
