from math import gcd

N = int(input())
A = tuple(map(int, input().split(' ')))

left = []
right = []

left.append(A[0])
for a in A[1:]:
    left.append(gcd(left[-1], a))

right.append(A[-1])
for a in A[-2::-1]:
    right.append(gcd(right[-1], a))

right = list(reversed(right))

ans = [left[-2], right[1]]

for i in range(1, len(left) - 1):
    ans.append(gcd(left[i - 1], right[i + 1]))

print(max(ans))
