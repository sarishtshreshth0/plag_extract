from itertools import accumulate


def LI():
    return list(map(int, input().split()))


N = int(input())
W = LI()
total = sum(W)
Wsum = list(accumulate(W))
ans = 10000000
for i in range(N):
    ans = min(ans, abs(Wsum[i]-(total-Wsum[i])))
print(ans)
