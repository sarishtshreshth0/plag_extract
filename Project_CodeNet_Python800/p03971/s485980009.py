n,A,B = map(int, input().split())
s = input()
a_count = 0
b_count = 0
for i in s:
  if i == 'a':
    if a_count + b_count < A + B:
      print('Yes')
      a_count += 1
    else:
      print('No')
  elif i == 'b':
    if a_count + b_count < A + B and b_count < B:
      print('Yes')
      b_count += 1
    else:
      print('No')
  else:
    print('No')