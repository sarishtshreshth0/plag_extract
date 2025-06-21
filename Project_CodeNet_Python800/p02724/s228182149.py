import sys
x = int(sys.stdin.read())
c500, x = divmod(x, 500)
c5 = x // 5
print(c500 * 1000 + c5 * 5)