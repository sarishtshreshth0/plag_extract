a, b, c, d = map(int, input().split())

if  a < c < b and c < b < d:
    print(b-c)
elif c < a < d and a < d < b:
    print(d-a)
elif a < c < d < b:
    print(d-c)
elif c < a < b < d:
    print(b-a)
elif a == c:
    print(min(b, d))
elif b == d:
    print(min(b-a,d-c))
else:
    print(0)