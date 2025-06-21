N = int(input())
W = [int(x) for x in input().split()]
WL = list(abs(sum(W[:x])-sum(W[x:])) for x in range(0,N+1))
print(min(WL))