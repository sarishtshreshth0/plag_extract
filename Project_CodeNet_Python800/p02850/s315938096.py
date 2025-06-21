import sys
sys.setrecursionlimit(2147483647)
INF=float('inf')
MOD=10**9+7
input=sys.stdin.readline

n=int(input())

#初期値が0の辞書
from collections import defaultdict
tree = defaultdict(lambda: set([])) 

color={}
key=[]

for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a-1].add(b-1)
    tree[b-1].add(a-1)
    color[(a-1,b-1)]=0
    key.append((a-1,b-1))

checked=[0]*n
cnt=0

def DEF(parent_color,node_no):
    global color,checked,tree,cnt
    checked[node_no]=1
    cnt=max(cnt,parent_color)
    i=1
    #print("node_no",node_no)
    for item in tree[node_no]:
        if checked[item]==0:
            if i==parent_color:
                i+=1
            
            color[(min(item,node_no),max(item,node_no))]=i
            DEF(i,item)
            i+=1
DEF(0,1)

print(cnt)
for item in key:
    print(color[item])

        






