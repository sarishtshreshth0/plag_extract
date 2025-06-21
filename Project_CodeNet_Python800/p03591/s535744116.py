import re

s = input()
pat = "YAKI"
m = re.match(pat, s)
if m:
	print("Yes")
else:
	print("No")