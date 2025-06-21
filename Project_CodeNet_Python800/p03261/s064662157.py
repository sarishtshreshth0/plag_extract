if __name__ == '__main__':

	n = int(input())
	s = input()
	A = []
	A.append(s)

	flg = True
	for _ in range(n-1):
		cmd = input()
		if s[-1] == cmd[0] and cmd not in A:
			A.append(cmd)
			s = cmd
		else:
			flg = False

	if flg :
		print("Yes")
	else:
		print("No")
