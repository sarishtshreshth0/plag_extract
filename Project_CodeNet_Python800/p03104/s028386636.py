def xor(n):
    if n == 0: return 0
    x = 0
    if ((n + 1) // 2) % 2 != 0: x = 1
    if n % 2 == 0: x ^= n
    return x

a, b = map(int, input().split())
print(xor(a - 1) ^ xor(b))
