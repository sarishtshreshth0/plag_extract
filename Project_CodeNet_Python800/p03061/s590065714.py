n = int(input())
a = list(map(int, input().split()))

import fractions
left, right = [], []
for arr, l in zip([a, a[::-1]], [left, right]):
    l.append(arr[0])
    for i in range(1, n):
        l.append(fractions.gcd(l[-1], arr[i]))

left = [right[-1], right[-2]] + left
right = right[::-1] + [left[-2], left[-1]]

ans = 0
for (l, r) in zip(left, right):
    ans = max(ans, fractions.gcd(l, r))

print(ans)
