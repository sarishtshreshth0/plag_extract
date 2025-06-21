a, b, c, d = map(int, input().split())

if a > c:
    right = a
elif a <= c:
    right = c

if b <= d:
    left = b
elif b > d:
    left = d

if right >= left:
    print(0)
elif right < left:
    print(left - right)