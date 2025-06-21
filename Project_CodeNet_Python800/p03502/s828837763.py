n = int(input())
m = n
cnt=0
while m:
	cnt += m % 10
	m //= 10
if n % cnt == 0:
	print("Yes")
else:
	print("No")