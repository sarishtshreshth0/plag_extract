A,B,C = input().split()
A,B,C = int(A),int(B),int(C)
if(((A<C)and(C<B))or((B<C)and(C<A))):
    print("Yes")
else:
    print("No")