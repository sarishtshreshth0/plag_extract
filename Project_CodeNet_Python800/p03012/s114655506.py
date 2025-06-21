N=int(input())
W=list(map(int,input().split()))

MIN=10**9
for i in range(1,N):
  diff = abs(sum(W[:i])-sum(W[i:]))
  if diff<MIN:MIN=diff
print(MIN)