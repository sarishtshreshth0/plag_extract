a, b = map(int, input().split())

fa = (a - 1) * ((a - 1) % 2 == 0) ^ a // 2 % 2
fb = b * (b % 2 == 0) ^ (b + 1) // 2 % 2
print(fa ^ fb)
