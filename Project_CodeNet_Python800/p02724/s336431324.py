# coding: utf-8

x = int(input())
ans = x // 500
x = x - ans * 500
ans = ans * 1000
ans += (x // 5 * 5)
print(ans)