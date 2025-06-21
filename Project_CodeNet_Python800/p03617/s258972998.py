q, h, s, d = list(map(int, input().split()))
n = int(input())
qpl = 4 * q
hpl = 2 * h
spl = s
dpl = d / 2
s_min = min(qpl, hpl, spl)
if dpl >= s_min:
    print(s_min * n)
elif n % 2 == 0:
    print(d * (n // 2))
else:
    print(d * (n // 2) + s_min)