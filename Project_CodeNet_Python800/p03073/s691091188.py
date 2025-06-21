import sys

S = str(input())
if len(S) == 1:
  print("0")
  sys.exit()
else:
  c1 = 0
  c2 = 0
  for i in range(len(S)):
    if i%2 == 0:
      if S[i] != "1":
        c1 += 1
    else:
      if S[i] != "0":
        c1 += 1
  for i in range(len(S)):
    if i%2 == 0:
      if S[i] != "0":
        c2 += 1
    else:
      if S[i] != "1":
        c2 += 1
print(min(c1,c2))