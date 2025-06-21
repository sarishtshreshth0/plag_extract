m, d = map(int, input().split())

s = 0
for i in range(1, d + 1):
    a = i % 10
    b = i // 10
    if (a > 1 and b > 1 and a * b <= m):
        s += 1
print(s)
