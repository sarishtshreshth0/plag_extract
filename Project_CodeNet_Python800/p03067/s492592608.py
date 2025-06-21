A, B, C = [int(a) for a in input().split()]
print("Yes" if (A<C and C<B) or (B<C and C<A) else "No")