N = int(input())
arr = list(map(int, input().split()))

ans = float('inf')

left = 0
right = sum(arr)

for i in range(N):
    left += arr[i]
    right -= arr[i]
    ans = min(ans, abs(left-right))

print(ans)