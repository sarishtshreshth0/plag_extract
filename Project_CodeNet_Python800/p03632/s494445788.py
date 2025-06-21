A,B,C,D=map(int,input().split())
if C<=B:
    if A<=C:
        if D>=B:
            print(B-C)
        else:
            print(D-C)
    else:
        if D>=B:
            print(B-A)
        elif A<=D<B:
            print(D-A)
        else:
            print(0)
else:
    print(0)