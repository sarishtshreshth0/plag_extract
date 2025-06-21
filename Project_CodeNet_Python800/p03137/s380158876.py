import heapq
n,m = map(int, raw_input().split(' '))

xis = map(int, raw_input().split())
xis.sort()
distances = [v- u for u,v in zip(xis,xis[1:])]
distances.sort(key = lambda x:-x)
print sum(distances[n-1:] or [0])