# ABC160

X = int(input())

ans = 0
coin_500 = 0
coin_5 = 0
coin_500 = X//500
X = X - coin_500*500
coin_5 = X//5
print(coin_500*1000+coin_5*5)