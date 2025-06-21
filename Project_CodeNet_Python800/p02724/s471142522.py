x = int(input())
t = x // 500
print(1000 * t + 5 * ((x - 500 * t) // 5))