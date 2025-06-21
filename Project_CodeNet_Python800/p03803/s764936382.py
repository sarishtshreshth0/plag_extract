arr = list(map(int, input().split()))
a = arr[0]
b = arr[1]

if 1 <= a <= 13 and 1 <= b <= 13:
  if a == b:
    print('Draw')
  elif a == 1:
    print('Alice')
  elif b == 1:
    print('Bob')
  elif a > b:
    print('Alice')
  elif b > a:
    print('Bob')