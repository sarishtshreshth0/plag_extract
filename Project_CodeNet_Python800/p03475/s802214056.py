n = int(input())
csf = [list(map(int, input().split())) for _ in range(n-1)]
 
for i in range(n):
    current = 0
    for j in range(i, n-1):
        if current < csf[j][1]:
            current = csf[j][1]
        if current % csf[j][2] != 0:
            current += csf[j][2] - (current % csf[j][2])
        current += csf[j][0]
    print(current)