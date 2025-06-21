import sys
a,b = map(int,input().split())
s = list(input())
if s[a] != "-":
	print("No")
	sys.exit()
s[a] = 1
if not "-" in s:
	print("Yes")
else:
	print("No")