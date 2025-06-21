A, B, C, D = map(int, input().split())

ans=0

if A<C:
    A=C
if D<B:
    B=D

if B<C or D<A:
    ans=0
else:
    ans=abs(A-B)

print(ans)