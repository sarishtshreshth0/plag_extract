
M,D = map(int,input().split())
count =0

for m in range(1,M+1):
    for d in range(21,D+1):
        d_10 = d//10
        d_1 = d%10
        if d_1 >1:
            if m == d_10 * d_1:
                count += 1
print(count)