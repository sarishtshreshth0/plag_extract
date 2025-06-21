n = input()
num = int(n)
s = sum(map(int, list(n)))
if num % s == 0:
  print("Yes")
else:
  print("No")