n = int(input())
r = []
b = []
for _ in range(n):
    x,y = map(int,input().split())
    r.append([x,y,0])
for _ in range(n):
    x,y = map(int,input().split())
    b.append([x,y])
r.sort(key=lambda x: x[1], reverse=True)
b.sort()
cnt = 0
for i in range(n):
    for j in range(n):
        if r[j][0] < b[i][0] and r[j][1] < b[i][1] and r[j][2]==0:
            cnt += 1
            r[j][2] = 1
            break
print(cnt)
