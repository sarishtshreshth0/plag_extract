n = int(input())
a = [list(map(int, input().split(' '))) for _ in range(n - 1)]

for i in range(n):
    # from i
    # now = 1ループごとにnow
    now = 0
    for j in range(i, n - 1):
        (c, s, f) = a[j]
        if now <= s:
            now = s + c
        else:
            # matsu
            now = s + (now - s + f - 1) // f * f + c
    print(now)
