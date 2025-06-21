q, h, s, d = map(int, input().split()); n = int(input())
h = min(q*2, h); s = min(h*2, s); d = min(s*2, d); x = 0
x += n//2*d; n %= 2; x += n//1*s
print(x)