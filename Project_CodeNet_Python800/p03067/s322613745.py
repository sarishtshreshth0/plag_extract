A,B,C=map(int, input().split())
if A<C and B>C:
  print('Yes')
elif B<C and A>C:
  print('Yes')
else:
  print('No')