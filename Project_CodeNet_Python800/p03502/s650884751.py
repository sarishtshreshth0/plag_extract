n = int(input())
m = n
r = 0
flg = True
while flg:
  a = n%10
  n //= 10
  r += a
  if n == 0:
    flg = False
if  m % r == 0:
  print('Yes')
else:
  print('No')