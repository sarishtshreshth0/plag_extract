N = int(input())
W = list(map(int, input().split()))

min = 999999999

for i in range(1, N):
    left = W[:i]
    right = W[i:]

    if abs(sum(left)-sum(right)) < min:
        min = abs(sum(left)-sum(right))


print(min)