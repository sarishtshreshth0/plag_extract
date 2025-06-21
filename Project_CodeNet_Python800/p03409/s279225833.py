N= int(input())
ab = [list(map(int,input().split())) for i in range(N)]
cd = [list(map(int,input().split())) for i in range(N)]
alr = [False for i in range(N)]
ab.sort()
cd.sort()
count = 0
for c,d in cd:
    maxi = -1
    maxb = -1
    for i in range(N):
        if alr[i]:
            continue
        a,b = ab[i][0],ab[i][1]
        if a < c:
            if b < d:
                if maxb < b:
                    maxb = b
                    maxi = i
        else:
            break
    if maxi != -1:
        alr[maxi] = True
print(alr.count(True))