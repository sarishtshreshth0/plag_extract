n=int(input())
ab = []
for _ in range(n):
    a, b = (int(x) for x in input().split())
    ab.append([a, b])
cd = []
for _ in range(n):
    c, d = (int(x) for x in input().split())
    cd.append([c, d])
ab = sorted(ab, key=lambda x: -x[0])
cd = sorted(cd, key=lambda x: x[1])

count = 0

for a, b in ab:
    index = -1
    for i, cda in enumerate(cd):
        if a < cda[0] and b < cda[1] :
            index = i
            break
    if index != -1:
        cd.pop(index)
        count += 1
print(count)