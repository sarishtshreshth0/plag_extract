q, h, s, d = map(int, input().split())
n = int(input())
l = min(q * 8, h * 4, s * 2, d)
if n % 2 == 0:
    print(l * n // 2)
else:
    if l == d:
        l2 = min(q * 4, h * 2, s)
        print(n // 2 * l + l2)
    else:
        print(l * n // 2)