N = int(input())
AB = []
CD = []
for i in range(N):
    AB.append(list(map(int,input().split())))
for i in range(N):
    CD.append(list(map(int,input().split())))

CD.sort(key=lambda x:x[0])

cnt = 0
RedDone = [0]*N
for i in range(N):
    Blue = CD[i]
    box = []
    for j in range(N):
        Red = AB[j]
        if Red[0]<Blue[0] and Red[1]<Blue[1] and RedDone[j]==0:
            box.append([Red[0],Red[1],j])
    if len(box)>0:
        maxy = -1
        cand = -1
        for k in range(len(box)):
            if RedDone[box[k][2]]==0:
                if maxy<box[k][1]:
                    cand = box[k][2]
                    maxy = box[k][1]
        cnt += 1
        RedDone[cand]=1
print(cnt)
