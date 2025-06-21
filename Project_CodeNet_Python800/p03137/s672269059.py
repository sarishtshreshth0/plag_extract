import heapq
n,m = map(int, raw_input().split(' '))

# I am given n pieces
if n >= m:
	print 0
else:
	xis = map(int, raw_input().split())
	xis.sort()


	distances = [v- u for u,v in zip(xis,xis[1:])]
	distances.sort(key = lambda x:-x)
	print sum(distances[n-1:] or [0])