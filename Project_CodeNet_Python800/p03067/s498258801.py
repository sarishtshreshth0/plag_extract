a, b, c = map(int, input().split())

if(a<b):
	for i in range(a, b):
		if i==c:
			print("Yes")
			exit()
if(a>b):
	for i in range(b, a):
		if i==c:
			print("Yes")
			exit()

print("No")
