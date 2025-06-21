

N = int(input())
red = []
blue = []
for i in range(N):
    a,b = map(int,input().split())
    red.append([a,b])
for i in range(N):
    c,d = map(int,input().split())
    blue.append([c,d])

blue.sort(key=lambda x: x[0])
used_red = [0]*N
for i in range(N):
    idx = -1
    for j in range(N):
        if used_red[j] != 0:
            continue
        if blue[i][0]-red[j][0]>0 and blue[i][1]-red[j][1]>0:
            if idx == -1 or red[idx][1]<red[j][1]:
                idx = j
    if idx!=-1:
        used_red[idx] += 1

print(sum(used_red))