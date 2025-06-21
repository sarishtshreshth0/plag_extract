n = int(input())
c = [0] * (n - 1)
s = [0] * (n - 1)
f = [0] * (n - 1)
for i in range(n - 1):
    c[i], s[i], f[i] = map(int, input().split())
for i in range(n - 1):
    a = 0
    for j in range(i, n - 1):
        if a <= s[j]:
            a = s[j]
        else:
            b = a - s[j]
            if b % f[j] > 0:
                a -= b
                a += (b // f[j]) * f[j]
                a += f[j]
        a += c[j]
    print(a)
print(0)