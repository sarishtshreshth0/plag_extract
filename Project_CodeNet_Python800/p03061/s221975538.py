N = int(input())
A = list(map(int,input().split()))

def gcd_(a, b):
    if a < b:    a, b = b, a
    if b == 0:    return a
    return gcd_(b, a % b)

left = [0 for _ in range(N + 1)]
right = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    left[i] = gcd_(left[i - 1], A[i - 1])
for i in reversed(range(N)):
    right[i] = gcd_(right[i + 1], A[i])

ans = -1
for i in range(N):
    ans = max(gcd_(left[i], right[i + 1]), ans)
print(ans)