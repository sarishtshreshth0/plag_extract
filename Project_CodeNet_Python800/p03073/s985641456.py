a = list(input())

n = len(a)

c = 0

for i in range(n):
    if (i % 2 == 0 and a[i] == "0") or (i % 2 == 1 and a[i] == "1"):
        c += 1

print(min(c, n-c))