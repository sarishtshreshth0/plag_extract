x = int(input())

money1 = x // 500
x %= 500
money2 = x // 5

ans = money1 * 1000 + money2 * 5
print(ans)