N, A, B = [int(x) for x in input().split()]
S = list(input())
go = 0
go_abroad = 0
for i in range(N):
  if(go)<(A+B):
    if(S[i]=='a'):
      print('Yes')
      go += 1
    elif(S[i]=='b') and (go_abroad<B):
      print('Yes')
      go += 1
      go_abroad += 1
    else:
      print('No')
  else:
    print('No')