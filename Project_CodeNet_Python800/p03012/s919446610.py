import itertools

n = int(input())
W = list(map(int, input().split()))

all = sum(W)
W_acc = list(itertools.accumulate(W))

dif = [(all-2*W_acc[i]) for i in range(n-1)]
ans = abs(min(dif, key = abs))
print(ans)