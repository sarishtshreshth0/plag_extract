x = int(input())

hc500 = x //  500
hc5 = (x - 500*hc500) // 5

print(hc500 * 1000 + hc5 * 5)
