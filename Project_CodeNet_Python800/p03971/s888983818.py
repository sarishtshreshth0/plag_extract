n, a, b = map(int, input().split())
s = input()

i = 0
j = 0
for n in s:
  if n == "a":
    if i + j < a + b:
      i += 1
      print("Yes")
    else:
      print("No")
  elif n == "b":
    if (i + j < a + b) and j < b:
      j += 1
      print("Yes")
    else:
      print("No")
  else:
    print("No")
