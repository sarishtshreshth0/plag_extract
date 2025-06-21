a = input().split()
b = int(a[0]) // 2
c = int(a[0]) % 2
if int(a[0]) == 1 or int(a[1]) == 1:
  print("1")
elif c == 0:
  print(int(int(b) * int(a[1])))
else:
  if int(a[1]) % 2 == 1:
    print(int(int(b) * int(a[1]) + int(a[1]) // 2 + 1))
  else:
    print(int(int(b) * int(a[1]) + int(a[1]) // 2))