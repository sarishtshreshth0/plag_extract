n, k = (int(n) for n in input().split())
count = 0
while True:
    n = n // k
    count += 1
    if n == 0:
        break
print(count)