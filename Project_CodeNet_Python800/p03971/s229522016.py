N,A,B=map(int,input().split())
S=input()

a,b=0,0
for i in range(N):
  if a+b<A+B:
    if S[i]=='a':
      print('Yes')
      a += 1
    elif S[i]=='b' and b < B:
      print('Yes')
      b += 1
    else:
      print('No')
  else:
    print('No')