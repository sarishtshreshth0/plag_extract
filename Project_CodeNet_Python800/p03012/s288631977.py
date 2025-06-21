n = int(input())
w = list(map(int, input().split()))
abs_diff = float('inf')
idx = 0
for i in range(n):
    if abs(sum(w[:i]) - sum(w[i:])) < abs_diff:
        abs_diff = abs(sum(w[:i]) - sum(w[i:]))
        idx = i
print(abs_diff)
