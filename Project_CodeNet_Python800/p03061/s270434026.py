from fractions import gcd
n = int(input())
an = list(map(int, input().split()))

left = [an[0]]
right = [an[-1]]
for i in range(1, n-1):
    left.append(gcd(left[-1], an[i]))
    right.append(gcd(right[-1], an[-(i+1)]))

ans = max(right[-1], left[-1])
for i in range(n-2):
    ans = max(ans, gcd(left[i], right[-(i+2)]))

print(ans)
