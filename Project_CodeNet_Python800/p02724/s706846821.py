x = int(input())

x, xm = divmod(x, 500)
y = xm // 5
print(x*1000 + y*5)