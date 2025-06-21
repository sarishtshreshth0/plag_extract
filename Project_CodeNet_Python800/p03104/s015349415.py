A, B = list(map(int, input().split()))

ans = 0


for i in range(1, 41):
    m = 2 ** (i-1)
    n = 2 * m
    a = (A // n) * m + max(0, A % n - m)
    b = ((B+1) // n) * m + max(0, (B+1) % n - m)

    if (b-a) % 2 == 1:
        ans += m

print(ans)
