def checkodd(num):
	if num%2:
		return True
	else:
		return False

A,B=map(int,input().split())

if checkodd(A) and checkodd(B):
	print("Yes")
else:
	print("No")
