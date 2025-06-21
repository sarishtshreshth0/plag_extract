S = input()
if len(S) <= 3:
  print("No")
  exit()
if S[:4] == "YAKI":
  print("Yes")
else:
  print("No")