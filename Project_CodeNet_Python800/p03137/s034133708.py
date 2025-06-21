if __name__ == '__main__':
	n,m = map(int,input().split())
	A = list(map(int,input().split()))
	A.sort()

	if n > m:
		print(0)
		exit()

	B = []
	for i in range(m-1):
		#差分を求める
		B.append(A[i+1] - A[i])
	B.sort()
	
	print(sum(B[:m-n]))
