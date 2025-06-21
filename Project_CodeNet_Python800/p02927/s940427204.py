M, D = map(int, input().split())
d10 = D // 10
d1 = D % 10
count = 0
if D >= 22:
    for i in range(4,M+1):
        for j in range(2, d10):
            for k in range(2, 10):
                if i == j * k:
                    count += 1
        for j in range(2, d1+1):
            if i == j * d10:
                count += 1

print(count)