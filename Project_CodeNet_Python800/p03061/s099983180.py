from fractions import gcd

N = int(input())
arr = list(map(int, input().split()))

left = [0 for _ in range(N+1)]
right = [0 for _ in range(N+1)]

for i in range(N):
  left[i+1] = gcd(left[i],arr[i])
  right[-i-2] = gcd(right[-i-1], arr[-i-1])

ans = 1
for i in range(N):
  result = gcd(left[i], right[i+1])
  ans = max(ans, result)

print(ans)