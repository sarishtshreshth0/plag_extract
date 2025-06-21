import sys, itertools

N = int(input())
W = list(map(int, sys.stdin.readline().rsplit()))

S = list(itertools.accumulate(W))

res = 10 ** 9
for i in range(N):
    res = min(res, abs(S[i] - (S[-1] - S[i])))

print(res)
