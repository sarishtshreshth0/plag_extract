from collections import defaultdict

N=int(input())
a=list(map(int,input().split()))

count=defaultdict(int)
for i in range(N):
  n = a[i]
  count[n-1] += 1
  count[n] += 1
  count[n+1] += 1

print(sorted(count.values())[-1])