n = int(input())
ps = []
for _ in range(n):
    a, b = map(int, input().split())
    ps.append([a, b, 0])
for _ in range(n):
    c, d = map(int, input().split())
    ps.append([c, d, 1])
ps = sorted(ps, key=lambda x: x[0])    

c = 0
for i in range(len(ps)):
    b = ps[i]
    # redもしくは、既にペアが決まっていたら飛ばす
    if b[2] == 0 or b[2] == 2:
        continue

    j = 0
    maxy = -1
    rec = -1
    while j < i:
        r = ps[j]
        # blue もしくは、既にペアが決まっていたら飛ばす
        if r[2] == 1 or r[2] == 2:
            j += 1
            continue

        if r[1] > maxy and r[1] < b[1]:
            maxy = r[1]
            rec = j
        j += 1
    if rec == -1:
        continue
    
    # ペアになったものを記録
    ps[rec][2] = 2
    c += 1
print(c)
