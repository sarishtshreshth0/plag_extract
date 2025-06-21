A, B, C, D = map(int, input().split())

if A <= C:
    if B < C:
        print(0)
    else:
        print(min(B, D) - C)
else:
    if D < A:
        print(0)
    else:
        print(min(B, D) - A)