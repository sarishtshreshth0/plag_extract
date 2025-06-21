N = int(input())
W = list(map(int, input().split()))

diff = sum(W)
for w in W:
    if diff > abs(diff-2*w):
        diff -= 2 * w
    else:
        break
print(abs(diff))