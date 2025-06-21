M, D = map(int, input().split())

count = 0
for m in range(4, M+1):
    for d in range(22, D+1):
        d_ten = d // 10
        d_one = d % 10
        if m == d_one * d_ten and (d_ten >= 2) and (d_one >= 2):
            count += 1
            
print(count)