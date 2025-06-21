A, B = input().split()

order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '1']

if A == B:
  print('Draw')
elif order.index(A) > order.index(B):
  print('Alice')
else:
  print('Bob')