n=int(input())
edges=[[] for i in range(1+n)]
e={}
for i in range(n-1):
    """#weighted->erase_,__,___=map(int,input().split())
    edges[_].append((__,___))
    edges[__].append((_,___))
    """
    _,__=map(int,input().split())
    edges[_].append(__)
    edges[__].append(_)
    e[(_,__)]=i
    e[(__,_)]=i
    """
"""#weighted->erase
f=max(len(j)for j in edges)
print(f)
ret=[0]*(n-1)
from collections import deque
dq=deque([(1,1)])
#pop/append/(append,pop)_left/in/len/count/[]/index/rotate()(右へnずらす)
while dq:
    a,c=dq.popleft()
    for to in edges[a]:
        if ret[e[(a,to)]]:continue
        ret[e[(a,to)]]=c
        c=c%f+1
        dq.append((to,c))
        
print(*ret,sep="\n")