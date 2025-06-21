A,B,C=map(int,input().split())
ans="No"
if A>B:
  if B<C and C<A:
    ans="Yes"
elif A<B:
  if A<C and C<B:
    ans="Yes"
print(ans)