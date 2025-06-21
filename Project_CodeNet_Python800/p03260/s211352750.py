if __name__ == '__main__':
	
	a,b = map(int,input().split())

	cnt = 0
	for c in range(1,4):
		if (a * b * c) % 2 == 1:
			print("Yes")
			break
	else:
		print("No")