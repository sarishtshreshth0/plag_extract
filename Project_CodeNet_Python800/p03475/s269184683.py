n = int(input())

c = [0] * n
f = [0] * n
s = [0] * n

for i in range(n - 1):
    c[i], s[i], f[i] = map(int, input().split())

lapse = [0] * n

for i in range(n):
    for j in range(i + 1, n):

        t = 0
        while s[j - 1] + t * f[j - 1] < lapse[i]:
            t += 1

        lapse[i] = s[j - 1] + t * f[j - 1] + c[j - 1]

    print(lapse[i])
