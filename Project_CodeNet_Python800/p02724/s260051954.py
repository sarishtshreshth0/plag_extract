x = int(input())
v500 = int(x // 500)
v5 = int((x % 500 ) //5)
print(v500 * 1000 + v5 * 5)