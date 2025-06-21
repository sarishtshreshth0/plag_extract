n, k = map(int, input().split())
count = 0
res = []
while True:
    if n < k ** count:
        print(count)
        break
    count += 1
