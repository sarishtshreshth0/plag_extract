A, B, C, D = map(int, input().split())
min_time = 0
if B > C and D > A:
    print(min(B, D) - max(A, C))
else:
    print(0)
