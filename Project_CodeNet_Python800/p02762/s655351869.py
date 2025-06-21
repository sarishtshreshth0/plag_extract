def main():
    N,M,K=map(int,input().split())

    G=[[] for i in range(N)]

    for i in range(M):
        a,b=map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    B=[[] for i in range(N)]
    for i in range(K):
        c,d=map(int,input().split())
        B[c-1].append(d-1)
        B[d-1].append(c-1)
    trace=[-1 for i in range(N)]
    Group=[]

    for i in range(N):
        stack=[]
        if trace[i]==-1:
            trace[i]=0
            stack.append(i)
        Group_tmp=[]
        while len(stack)>0:
            index=stack.pop()
            Group_tmp.append(index)
            for j in G[index]:
                if trace[j]==-1:
                    trace[j]=0
                    stack.append(j)
        if len(Group_tmp)!=0:
            Group.append(Group_tmp)
    res=[0 for i in range(N)]
    GroupMarker=[-1 for i in range(N)]

    for i in range(len(Group)):
        for j in range(len(Group[i])):
            person=Group[i][j]
            GroupMarker[person]=i
            r=len(Group[i])-len(G[person])-1
            res[person]=r

    for i in range(len(B)):
        for j in range(len(B[i])):
            if GroupMarker[i]==GroupMarker[B[i][j]]:
                res[i]-=1
    res=list(map(str,res))
    print(" ".join(res))

if __name__=="__main__":
    main()



