x = int(input())
ans = 0

a = int(x / 500)
ans = ans + a * 1000

x = x % 500
b = int(x / 5)
ans = ans + b * 5

print(ans)