q, h, s, d = map(int, input().split())
n = int(input())

#2Lあたりの金額の最小値
x = min(q * 8, h * 4, s * 2, d)
#1Lあたりの金額の最小値
y = min(q * 4, h * 2, s)

if n == 1:
    print(y)
else:
    if n % 2 == 0:
        print(x * (n // 2))
    else:
        print(x * (n // 2) + y)

