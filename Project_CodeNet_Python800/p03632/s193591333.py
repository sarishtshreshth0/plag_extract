a, b, c, d = map(int, input().split())
table = [0] * 101

for i in range(a, b+1):
    table[i] += 1

for j in range(c, d+1):
    table[j] += 1

print(table.count(2) if table.count(2) == 0 else table.count(2)-1)