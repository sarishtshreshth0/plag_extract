from sys import stdin
import sys
import copy
sys.setrecursionlimit(200000)
N,M,K=list(map(int,input().split()))
counter=[[None,None] for i in range(N+1)]
friend_list=[set() for _ in range(N+1)]
block_list=[set() for _ in range(N+1)]
def friend_tansaku(i,j):
    color.add(j)
    cnt[0]+=1
    for friend in friend_list[j]:
        if friend not in color :
            friend_tansaku(i,friend)





for _ in range(M):
   a,b= list(map(int, input().split()))
   friend_list[a].add(b)
   friend_list[b].add(a)
for _ in range(K):
    a, b = list(map(int, input().split()))
    block_list[a].add(b)
    block_list[b].add(a)
for i in range(1,N+1):
    cnt=[0]
    color =set()
    if counter[i][0] is None:
        friend_tansaku(i,i)
        cnt=cnt[0]
        for aa in color:
            counter[aa]=[color,cnt]
    color,cnt =counter[i][0],counter[i][1]
    for k in block_list[i]:
        if k not in color:
            cnt+=1

    count=cnt-(len(friend_list[i])+len(block_list[i]))-1
    if i==N:print(count)
    else:print(count,end=" ")