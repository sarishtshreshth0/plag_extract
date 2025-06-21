import string

A,B=list(map(int, input().split()))
S=input()
a=S[:A]
hi=S[A]
b=S[A+1:]
L=string.digits

if all(a[_] in L for _ in range(A)) and \
   all(b[_] in L for _  in range(B)) and \
   hi=='-':
  print('Yes')
else:
  print('No')