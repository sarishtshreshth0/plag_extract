import sys

s = input()

if len(s) < 4:
	print("No")
	sys.exit()

if s[:4] == "YAKI":
	print("Yes")
else:
	print("No")