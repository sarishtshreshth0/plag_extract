N = int(input())
W = list(map(int, input().split()))

avg = sum(W) / 2
total = 0

for i in range(N):
    total += W[i]
    if total >= avg:
        a = total
        b = total - W[i]
        break

print(min(2 * a - sum(W), sum(W) - 2 * b))
