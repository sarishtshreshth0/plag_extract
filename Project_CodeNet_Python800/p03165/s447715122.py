import sys
import math
from  collections import defaultdict

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


def solve(test):
	s = [''] + list(input())
	t = [''] + list(input())
	rec = [[0 for j in range(len(t))] for i in range(len(s))]
	for i in range(1, len(s)):
		for j in range(1, len(t)):
			if s[i] == t[j]:
				rec[i][j] = 1 + rec[i - 1][j - 1]
			else:
				rec[i][j] = max(rec[i - 1][j], rec[i][j - 1])

	ans = []
	i, j = len(s) - 1, len(t) - 1
	while i >= 0 and j >= 0:
		if s[i] == t[j]:
			ans.append(s[i])
			i -= 1
			j -= 1
		elif rec[i - 1][j] > rec[i][j - 1]:
			i -= 1
		else:
			j -= 1

	print(''.join(ans[::-1]))


if __name__ == "__main__":
	test_cases = 1
	for t in range(1, test_cases + 1):
		solve(t)
