from operator import itemgetter
N = int(input())
Red = [list(map(int,input().split())) for _ in range(N)] #赤
Blue = [list(map(int,input().split())) for _ in range(N)] #青

Red1 = sorted(Red, key=itemgetter(1),reverse = True)
Blue1 = sorted(Blue, key=itemgetter(0),reverse = False)

cnt = 0
for i in range(N):
    for j in range(N):
        if Red1[i][1] < Blue1[j][1] and  Red1[i][0] < Blue1[j][0] :
            cnt += 1
            Blue1[j][0] = -1
            break
print(cnt)