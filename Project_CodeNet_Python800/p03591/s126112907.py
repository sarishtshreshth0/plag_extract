def solution():
	s = list(input().strip())
	if len(s) < 4:
		print('No')
	else:
		s = ''.join(s[:4])
		if s == 'YAKI':
			print('Yes')
		else:
			print('No')



solution()