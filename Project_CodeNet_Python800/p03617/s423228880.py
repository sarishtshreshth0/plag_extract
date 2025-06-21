Q, H, S, D = map(int, input().split())
n = int(input())
coffee = [[Q*4, 0.25, Q], [H*2, 0.5, H], [S, 1, S], [D/2, 2, D]]
coffee_cost = sorted(coffee)
cost = 0
Qt = n
for i in range(4):
    cost += (round(Qt // coffee_cost[i][1]) * coffee_cost[i][2])
    Qt = round(Qt % coffee_cost[i][1])
    if Qt == 0:
        print(int(cost))
        exit()
