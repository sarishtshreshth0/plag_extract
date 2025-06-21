x = int(input())

a = x // 500
b = (x - (a * 500)) // 5
c = (a * 1000) + (b * 5)
print(c)