#

import sys
input=sys.stdin.readline
from collections import deque

def main():
    N,M,K=map(int,input().split())
    ABadj=[[] for i in range(N)]
    CDadj=[set() for i in range(N)]
    for i in range(M):
        a,b=map(int,input().split())
        ABadj[a-1].append(b-1)
        ABadj[b-1].append(a-1)
    for i in range(K):
        c,d=map(int,input().split())
        CDadj[c-1].add(d-1)
        CDadj[d-1].add(c-1)
    
    w=[-1]*N
    sets=[]
    j=-1
    done=[-1]*N
    for i in range(N):
        if done[i]==-1:
            sets.append(set())
            j+=1
            qu=deque([i])
            done[i]=1
            sets[j].add(i)
            w[i]=j
            while(len(qu)>0):
                v=qu.popleft()
                for nv in ABadj[v]:
                    if done[nv]==-1:
                        done[nv]=1
                        qu.append(nv)
                        sets[j].add(nv)
                        w[nv]=j
    
    for i in range(N):
        ans=len(sets[w[i]])-1-len(ABadj[i])
        for bl in CDadj[i]:
            if bl in sets[w[i]]:
                ans-=1
        print(ans,end=" ")
            
    
    
    
if __name__=="__main__":
    main()
