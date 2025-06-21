a = input().split()
b = input()
c = int(0)

for i in range(int(a[0])):
  if b[i] == "-":
    c = 1
  else:
    pass

if b[int(a[0])] != "-":
  c = 1

for i in range(int(a[0]) + 1, int(a[0]) + int(a[1]) + 1):
  if b[i] == "-":
    c = 1
  else:
    pass

if c == 1:
  print("No")
else:
  print("Yes")