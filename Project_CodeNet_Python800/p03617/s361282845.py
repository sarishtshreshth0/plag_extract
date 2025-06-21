def resolve():
    q, h, s, d = map(int, input().split())
    n = int(input())
    h = min(h, 2*q)
    s = min(s, h*2)
    if s*2 <= d:
        print(s*n)
    else:
        print(d*(n//2) + s*(n%2))
resolve()