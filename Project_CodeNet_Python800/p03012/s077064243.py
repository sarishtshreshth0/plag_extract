n = int(input())
weight = list(map(int, input().split()))

s = [0] * (n+1)
total = 0
for i in range(0, n):
    s[i+1] = s[i] + weight[i]
    total += weight[i]

minimum_weight = total

for i in range(1, n):
    minimum_weight = min(minimum_weight, abs(s[i] - (total - s[i])))

print(minimum_weight)