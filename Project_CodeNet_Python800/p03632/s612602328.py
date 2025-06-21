A, B, C, D = map(int, input().split())
if A <= C < D <= B:
    print(D - C)
elif C <= A < B <= D:
    print(B - A)
elif A <= C <= B <= D:
    print(B - C)
elif C <= A <= D <= B:
    print(D- A)
else:
    print(0)