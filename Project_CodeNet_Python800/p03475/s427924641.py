n = int(input())

csfn = [None] * (n - 1)
for i in range(n - 1):
    csfn[i] = list(map(int, input().split(' ')))

result = [0] * n

for i in range(n - 1):
    for j in range(0, i + 1):
        if csfn[i][1] > result[j]:
            result[j] += (csfn[i][1] - result[j])
        else:
            result[j] += (-result[j] % csfn[i][2])
        result[j] += csfn[i][0]
        
for r in result:
    print(r)


    
