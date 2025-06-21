s = input()
a = 0
b = 0
for i in range(len(s)):
  if i % 2 == 0:
    if s[i] == "0":
      a = a+1
    else:
      b = b+1
  else:
    if s[i] == "0":
      b = b+1
    else:
      a = a+1
if a < b:
  print(a)
else:
  print(b)