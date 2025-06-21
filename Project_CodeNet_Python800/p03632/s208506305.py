A, B, C, D = map(int, input().split())
if A < C:
    if B < D:
        if C < B:
            print(B-C)
        else:
            print(0)
    else:
        print(D-C)
else:
    if D < B:
        if A < D:
            print(D-A)
        else:
            print(0)
    else:
        print(B-A)