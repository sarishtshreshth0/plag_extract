n, k = map(int, input().split())
count = 1
while n >= k:
    n, _ = divmod(n, k)
    count += 1
print(count)
