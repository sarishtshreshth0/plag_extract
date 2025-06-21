from itertools import accumulate
N = int(input())
W = list(map(int, input().split()))
S = list(accumulate(W))
print(min(abs(S[-1]-s-s) for s in S[:-1]))