a, b, c, d = map(int, input().split())
if a >= c:
    if b >= d:
        print(max(d-a, 0))
    else:
        print(max(b-a, 0))
else:
    if b >= d:
        print(max(d-c, 0))
    else:
        print(max(b-c, 0))