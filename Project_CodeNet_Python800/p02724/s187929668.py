x = int(input())

x500 = x // 500
y = x - x500*500
y5 = y // 5
z = y - y5*5

print(x500*1000+y5*5)