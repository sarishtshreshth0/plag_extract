s = input()
len_s = len(s)
if len_s >= 4:
  if s[:4] == "YAKI":
    print("Yes")
  else:
    print("No")
else:
  print("No")