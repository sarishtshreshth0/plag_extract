A,B,C,D = map(int,input().split())
if B<=C or A>=D:
    print(0)
elif A<C<B<D:
    print(B-C)
elif C<A<D<B:
    print(D-A)
else:
    print(min(D-C,B-A))