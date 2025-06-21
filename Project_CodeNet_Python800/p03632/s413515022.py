a, b, c, d = map(int, input().split())

st = max(a, c)
ed = min(b, d)

if ed - st > 0:
    print(ed-st)
else:
    print(0)