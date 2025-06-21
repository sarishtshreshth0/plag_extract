x = int(input())

big = x // 500

small = (x - (big*500)) // 5

print(big*1000 + small*5)
