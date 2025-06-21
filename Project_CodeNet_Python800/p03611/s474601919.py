import collections
n = int(input())
a = list(map(int,input().split()))
M = 1

c = collections.Counter(a)

for x in range(max(a) + 2):
	d = c[x] + c[x-1] + c[x+1]
	if d >= M:
		M = d

print(M)