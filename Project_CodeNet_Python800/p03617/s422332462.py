import sys
input = sys.stdin.readline

# A - Ice Tea Store
prices = list(map(int, input().split()))
n = int(input())

stores = []
units = [1, 2, 4, 8]
magnifications = list(reversed(units))

for i in range(4):
	compared_price = prices[i] * magnifications[i]
	store = [units[i], prices[i], compared_price]
	stores.append(store)

# 0:購入単位, 1:価格, 2:比較用の価格
stores.sort(key=lambda x:x[2])

amount = n * 4
ans = 0

for i in range(4):
	unit = stores[i][0]
	price = stores[i][1]

	ans += price * (amount//unit)
	amount %= unit

print(ans)