from sys import stdin
from collections import deque
def main():
    #入力
    readline=stdin.readline
    N=int(readline())
    g=[[] for _ in range(N)]
    AB=[]
    for _ in range(N-1):
        a,b=map(lambda x:int(x)-1,readline().split())
        g[a].append(b)
        g[b].append(a)
        AB.append(str(a)+" "+str(b))

    link=[0]*N
    que=deque([0])
    is_searched=[False]*N
    is_searched[0]=True
    K=0
    ans=dict()
    #bfs
    while len(que)>=1:
        now=que.popleft()
        color=1
        for x in g[now]:
            if is_searched[x]:
                continue
            else:
                is_searched[x]=True
                que.append(x)
                if color==link[now]:
                    color+=1
                link[x]=color
                ans[str(min(now,x))+" "+str(max(now,x))]=color
                color+=1
        color-=1
        K=max(K,color)

    #出力
    print(K)
    for key in AB:
        print(ans[key])
        
if __name__=="__main__":
    main()