# ANSHUL GAUTAM
# IIIT-D

from math import *
from copy import *
from heapq import *
from string import *				# alpha = ascii_lowercase
from random import *				# l.sort(key=lambda l1:l1[0]-l1[1]) => ex: sort on the basis difference
from bisect import *				# bisect_left(arr,x,start,end)  => start and end parameters are temporary
from sys import stdin				# bisect_left return leftmost position where x should be inserted to keep sorted
from sys import maxsize
from operator import *				# d = sorted(d.items(), key=itemgetter(1))
from itertools import *
from collections import Counter		# d = dict(Counter(l))
from collections import defaultdict # d = defaultdict(list)

'''
3 4
4 3
4 1
2 2
'''

def solve(l,m):
	n = len(l)
	L = [[] for i in range(10**5+1)]
	for i in l:
		d,r = i
		L[d].append(r)
	ans = 0
	hp = []
	for i in range(1,m+1):
		for j in L[i]:
			heappush(hp,-j)
		if(hp):
			ans -= heappop(hp)
	return ans

N,M = list(map(int, stdin.readline().rstrip().split()))
l = []
for _ in range(N):
	a,b = list(map(int, stdin.readline().rstrip().split()))
	l.append([a,b])
ans = solve(l,M)
print(ans)
