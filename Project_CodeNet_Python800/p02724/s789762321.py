x = int(input())

div, mod = divmod(x, 500)

print(div * 1000 + mod // 5 * 5)