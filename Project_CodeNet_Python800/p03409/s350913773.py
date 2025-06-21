INF=10**30
N=int(input())
ball=[list(map(int,input().split()))+['r'] for i in range(N)]
ball[len(ball):len(ball)]=[list(map(int,input().split()))+['b'] for i in range(N)]
ball.sort(key=lambda x:x[0])
cnt=0
for i in range(len(ball)):
    if(ball[i][2]=='b'):
        match=INF
        Ym=-1
        for j in range(i):
            if(ball[j][2]=='r'):
                if(ball[j][1]>Ym and ball[i][1]>ball[j][1]):
                    Ym=ball[j][1]
                    match=j
        if(match!=INF):
            ball[match][1]=INF
            cnt+=1
print(cnt)