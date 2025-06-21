a,b=map(int,input().split())
s=input()
if s[a]=="-" and str.isdecimal(s[:a]+s[-b:]):
	print("Yes")
else:
	print("No")