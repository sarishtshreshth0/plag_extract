n = int(input())
p = n // 500 * 1000
n %= 500
p += n // 5 * 5
print(p)