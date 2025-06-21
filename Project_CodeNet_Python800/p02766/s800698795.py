n, k = map(int, input().split())
x = k
i = 1
while n >= x:
    i += 1
    x *= k
print(i)