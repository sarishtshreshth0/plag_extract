n = int(input())

table = []
for i in range(n-1):
    c , s , f = map(int,input().split())
    table.append([c,s,f])

for i in range(n):
    time = 0
    for j in range(i,n-1):
        if time < table[j][1]:
            time = table[j][1]
        elif time > table[j][1]:
            if time % table[j][2] != 0:
                time += table[j][2] -(time%table[j][2])
        time += table[j][0]
    print(time)