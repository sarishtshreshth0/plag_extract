A,B,C,D=map(int,input().split())
if C<=A and B<=D:
  print(B-A)
elif C<D<=A<B:
  print(0)
elif C<=A and D<=B:
  print(D-A)
elif B-C>=0 and B<=D:
  print(B-C)
elif B-C>=0 and B>=D:
  print(D-C)
else:
  print(0)