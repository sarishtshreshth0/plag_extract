def xorsum(n):
    if n % 2:
        return 0 if (n // 2) % 2 else 1
    else:
        return n + 1 if (n // 2) % 2 else n

a, b = map(int, input().split())
if a != 0:
    print(xorsum(b) ^ xorsum(a - 1))
else:
    print(xorsum(b))
