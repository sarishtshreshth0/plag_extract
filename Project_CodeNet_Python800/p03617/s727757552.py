q, h, s, d, n = map(int, open(0).read().split())
print(min(8 * q, 4 * h, 2 * s, d) * (n // 2) + min(4 * q, 2 * h, s) * (n % 2))