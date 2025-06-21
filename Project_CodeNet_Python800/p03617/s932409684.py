price = [int(w) for w in input().split()]
n = int(input())
price[0]*=4
price[1]*=2
cheap = min(price[:3])

ans = n // 2 * min(cheap * 2, price[3])
ans += n % 2 * cheap


print(ans)
