MD = [int(i) for i in input().split(' ')]
M = [int(i)+1 for i in range(MD[0])]
D = [int(i)+1 for i in range(MD[1])]

count = 0
for d in D:
    if d // 10 >= 2 and d % 10 >= 2:
        d2 = d // 10
        d1 = d % 10
        if d1*d2 in M:
            count+=1

print(count)