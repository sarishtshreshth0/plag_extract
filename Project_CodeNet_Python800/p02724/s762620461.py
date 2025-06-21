x = int(input())
v, m = x // 500 * 1000, x % 500
v += m // 5 * 5
print(v)
