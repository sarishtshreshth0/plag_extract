n = int(input())
ab = []
cd = []
ans = 0
item = set()

for _ in range(n):
    a,b = map(int,input().split())
    ab.append((a,b))

for _ in range(n):                                                                                                               
    c,d = map(int,input().split())
    cd.append((c,d))

cd.sort()

for i in cd:
    c,d = i
    li = []
    for j in ab:
        a,b = j
        if a < c and b < d:
            li.append((a,b))
    li.sort(key=lambda x:(x[1]*(-1),x[0]))
    for k in li:
        if k not in item:
            ans += 1
            item.add(k)
            break

print(ans)