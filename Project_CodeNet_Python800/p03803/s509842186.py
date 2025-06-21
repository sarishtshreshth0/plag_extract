a, b = map(int, input().split())
lst = [i for i in range(2, 14)] + [1]
if a == b:
  print('Draw')
else:
  print(['Bob', 'Alice'][lst.index(a) > lst.index(b)])