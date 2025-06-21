# ABC070B

a, b, c, d = map(int, input().split())
if b <= c: # a-b c-d
    print(0)
elif a <= c <= b and c <= b <= d: # a-c-b-d
    print(b - c)
elif a <= c <= d <= b: # a-c-d-b
    print(d - c)
elif c <= a <= b <= d: # c-a-b-d
    print(b - a)
elif c <= a <= d <= b: # c-a-d-b
    print(d - a)
elif c <= a <= b <= d: # c-a-b-d
    print(b - a)
elif c <= d <= a <= b: # c-d a-b
    print(0)
else:
    print(a, b, c, d)
