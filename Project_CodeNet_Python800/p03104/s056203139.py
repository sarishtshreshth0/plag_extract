A,B=[int(x) for x in input().split()]

if A==B:
	print(A)
	exit()

if A%2==1 and B%2==1:
	even=(B-A)//2
else:
	even=(B-A)//2+1

if even%2==0:	
	if A%2==1 and B%2==0:
		print(A^B^1)
	elif A%2==1 and B%2==1:
		print(A)
	elif A%2==0 and B%2==1:
		print(0)
	elif A%2==0 and B%2==0:
		print(B^1)
else:
	if A%2==1 and B%2==0:
		print(A^B)
	elif A%2==1 and B%2==1:
		print(A^1)
	elif A%2==0 and B%2==1:
		print(1)
	elif A%2==0 and B%2==0:
		print(B)