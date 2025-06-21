S = input()
a = 0
b = 0
for i, s in enumerate(S):
  if i % 2:
    if s == "1":
      a += 1
    else:
      b += 1
  else:
    if s == "1":
      b += 1
    else:
      a += 1
print(min(a, b))