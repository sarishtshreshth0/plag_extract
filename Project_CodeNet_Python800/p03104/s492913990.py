a, b = map(int, input().split())
x = 0
if  a == b:
    print(a)
else:
    if a % 2 == 1:
        x ^= a
        a += 1
    if b % 2 == 0:
        x ^= b
        b -= 1
    num = b - a + 1
    num //= 2
    if num %2 == 1:
        x ^= 1
    print(x)
