M,N = map(int,input().split())

if M == N:
  print('Draw')
elif (M>N and N!=1) or M==1:
  print('Alice')
else:
  print('Bob')