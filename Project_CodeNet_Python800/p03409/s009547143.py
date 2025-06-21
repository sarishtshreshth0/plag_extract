from collections import defaultdict
n = int(input())
cnt = 0
dic = defaultdict(list)
ab = []
cd = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))
for i in range(n):
    c, d = map(int, input().split())
    cd.append((c, d))
for i in ab:
    for j in cd:
        a, b = i
        c, d = j
        if a < c and b < d:
            dic[i].append(j)
seen = set()
for key, value in sorted(dic.items(), key=lambda x: x[0][1], reverse=True):
    for co in sorted(value, key=lambda x: x[0]):
        if co not in seen:
            cnt += 1
            seen.add(co)
            break
print(cnt)


