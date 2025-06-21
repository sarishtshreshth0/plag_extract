
if __name__ == '__main__':

	n,k = map(int,input().split())

	cnt = 1
	while True:
		if n % k == 0:
			n = n // k
		else:
			n = n - n % k
			n = n // k
		if n // k < k:
			if n // k == 0:
				if n % k == 0:
					pass
				else:
					cnt += 1
			else:
				cnt += 2
			break
		cnt += 1
			
	print(cnt)
