"""
500 -> 1000
5 -> 5
"""
ans = 0
n = int(input())
if n >= 500:
    goh = n // 500
    zan = n % 500
    ans += goh*1000
    n = zan
if n < 500 and n != 0:
    g = n // 5
    ans += g*5

print(ans)