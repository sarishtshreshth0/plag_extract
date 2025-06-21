h, m = map(int, input().split())

if h == 1 or m == 1:
    count = 1
else:
    count = ((h //2) * m) + ((h %2) *((m //2) + (m %2)))
print(count)
