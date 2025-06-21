A, B, C, D = map(int, input().split())
if A<C and C<B:
    if B<D:
        print(B-C)
    else:
        print(D-C)
elif C<=A and A<D:
    if  D<B:
        print(D-A)
    else:
        print(B-A)
else:
    print(0)