A, B, C, D = map(int, input().split())
if A > C:
    A, B, C, D = C, D, A, B
print(max(0, min(D, B)-C))
