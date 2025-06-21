N = int (input())
W = list(map(int, input().split()))
w = 0
for i in range(N - 1):
    w += W[i]
    if w > sum(W) / 2:
        break
print(min(abs(sum(W[0: i]) - sum(W[i: N])), abs(sum(W[0: i + 1]) - sum(W[i + 1: N]))))