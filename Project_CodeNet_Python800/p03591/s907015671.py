import re

str = input()

m = re.match("^YAKI",str)

if m:
  print("Yes")
else:
  print("No")