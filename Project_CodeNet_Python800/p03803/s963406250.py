n = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
A, B = map(int, input().split())
idxa = n.index(A)
idxb = n.index(B)

if idxa > idxb:
  print('Alice')
elif idxa == idxb:
  print('Draw')
else:
  print('Bob')