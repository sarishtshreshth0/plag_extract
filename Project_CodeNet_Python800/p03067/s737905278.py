#2019/10/15
A,B,C = map(int, open(0).read().split())
print("Yes" if A<C<B or A>C>B else "No")