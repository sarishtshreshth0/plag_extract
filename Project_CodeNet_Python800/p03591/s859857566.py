S = input()
if len(S) <= 3:
  print("No")
  exit()
print("Yes" if S[:4] == "YAKI" else "No")