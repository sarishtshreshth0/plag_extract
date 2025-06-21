A, B, C, D = map(int, input().split())
if B <= C or D <= A:
    print(0)
elif A <= C:
    if B <= D:
        print(B - C)
    else:
        print(D - C)
else:
    if D <= B:
        print(D - A)
    else:
        print(B - A)
