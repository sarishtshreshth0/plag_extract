A, B, C = map(int, input().split())
ans = ''
if A<C<B or B<C<A:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)