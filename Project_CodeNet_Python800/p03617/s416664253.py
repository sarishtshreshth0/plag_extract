Q, H, S, D = map(int, input().split())
prices = {0.25: Q, 0.5: H, 1: S, 2: D}
n = int(input())
costs = {0.25: Q * 8, 0.5: H * 4, 1: S * 2, 2: D}
costs_sorted = sorted(costs.items(), key=lambda x: x[1])
ans = 0
for cost in costs_sorted:
    quantity = cost[0]
    div, n = divmod(n, quantity)
    ans += int(prices[quantity] * div)
    if n == 0:
        break

print(ans)
