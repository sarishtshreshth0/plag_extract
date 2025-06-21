import sys
sys.setrecursionlimit(10**9)
N = int(input())
nood = [[]for i in range(0,N+1,1)]
h_color = [1]*(N+1)
for i in range(1,N,1):
    a,b=map(int,input().split())
    nood[a].append([b,i])
    nood[b].append([a,i])

max_color_count = -1

def bfs(nowNood,preNood,preColor):
    global max_color_count
    colorCount=1
    for i in range(0,len(nood[nowNood]),1):
        if nood[nowNood][i][0]!=preNood:
            if colorCount == preColor:
                colorCount+=1
            h_color[nood[nowNood][i][1]]=colorCount
            bfs(nood[nowNood][i][0],nowNood,colorCount)
            max_color_count = max(max_color_count,colorCount)
            colorCount+=1

bfs(1,-1,-1)
print(max_color_count)
for i in range(1,N,1):
    print(h_color[i])