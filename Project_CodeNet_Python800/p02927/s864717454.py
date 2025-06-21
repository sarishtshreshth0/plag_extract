m,d = map(int,input().split(" "))
if d <= 19:
    print(0)
    exit()
count = 0
for i in range(22,d+1):
    if i // 10 >= 2 and i % 10 >= 2:
        if (i // 10) * (i % 10) <= m:
            count += 1
print(count)