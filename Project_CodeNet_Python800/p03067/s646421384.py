a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
if a > c:
  # 下る場合
  if b < c:
    print('Yes')
  else:
    print('No')
else:
  # 上る場合
  if b > c:
    print('Yes')
  else:
    print('No')