N = int(input())
W = list(map(int, input().split()))

res = 101
for i in range(len(W)):
    left  = sum(W[:i])
    right = sum(W[i:])
    if res > abs(left-right):
        res = abs(left-right)

print(res)