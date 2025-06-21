A, B, C, D = map(int, input().split())

"""
count = 0

for i in range(0,101):
    if A <= i and i < B and C <= i and i < D:
        count += 1

print(count)
"""

lower = max(A, C)
upper = min(B, D)

ans = max(0, upper - lower)

print(ans)