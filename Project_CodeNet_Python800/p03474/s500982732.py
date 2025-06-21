A,B=map(int,input().split())
S=input()


if S[A]=="-" and str.isdecimal(S[:A]+S[-B:]):
	print("Yes")
else:
	print("No")