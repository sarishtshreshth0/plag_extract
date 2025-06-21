n, k = map(int, input().split())
if n < k:
    print(1)
    exit()
v = []
while True:
    x = n % k
    n //= k
    v.append(x)
    if n < k:
        v.append(n)
        break
print(len(v))
