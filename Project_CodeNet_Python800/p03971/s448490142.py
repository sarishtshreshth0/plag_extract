N, A, B = map(int, input().split())
S = list(input())
cy = 0
co = 0
for i in range(N):
  if S[i]=='a':
    if cy < A+B:
      cy += 1
      print('Yes')
    else:
      print('No')
  if S[i]=='b':
    if cy < A+B and co < B:
      cy += 1
      co += 1
      print('Yes')
    else:
      print('No')
  if S[i]=='c':
    print('No')
