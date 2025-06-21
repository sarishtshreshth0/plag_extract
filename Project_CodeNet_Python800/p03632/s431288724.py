A, B, C, D = map(int, input().split())

seconds = min(B, D) - max(A, C)

if seconds <= 0:
    seconds = 0

print(seconds)