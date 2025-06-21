def resolve():
    a, b, c, d = map(int, input().split())
    ans = int()
    if c < a:
        if d <= a:
            ans = 0
        elif a < d and d <= b:
            ans = d-a
        elif b < d:
            ans = b-a
    elif a <= c:
        if d <= b:
            ans = d-c
        elif b < d:
            ans = b-c
    if b <= c:
        ans = 0
    print(ans)
resolve()