M, D = map(int, input().split())
count = 0
for i in range(M+1):
    for j in range(D+1):
        d10 = int(j /10)
        d1 = int(j % 10)
        if d10 >=2 and d1 >=2 and d10 * d1 ==i:
            count += 1
print(count)