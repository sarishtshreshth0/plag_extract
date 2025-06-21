A,B,C,D=map(int,input().split())
if B<C or D<A:
    print(0)
    exit()
else:
    start=max(A,C)
    end=min(B,D)
print(end-start)