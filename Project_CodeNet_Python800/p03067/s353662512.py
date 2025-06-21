a,b,c = map(int,input().split())
if(b < c and a > c):
	print("Yes")
elif(a < c and b > c):
	print("Yes")
else:
	print("No")