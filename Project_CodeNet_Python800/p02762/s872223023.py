from collections import deque

N,M,K = list(map(int,input().split()))

# N,M,K = [10,random.randint(1,10),random.randint(1,10)]

ad={} #友達関係
block={} #ブロック
for n in range(N):
    n=n+1
    ad[n]=set([])
    block[n]=set([])
    
for m in range(M):
    m1,m2 = list(map(int,input().split()))
    ad[m1].add(m2)
    ad[m2].add(m1)

for k in range(K):
    k1,k2 = list(map(int,input().split()))
    block[k1].add(k2)
    block[k2].add(k1)

visit = deque([])
color={}
tree={}
t=0
for n in range(N):
    n=n+1
    color[n] = -1
    tree[n] = -1
    
start_ = 1
    
while len(visit) < N:
    t += 1
    for c_k in range(start_,N):
        if color[c_k] == -1:
            start = c_k
            start_ = start + 1
            break
    color[start] = 0
    tree[start] = t
    visit_temp=deque([start])

    while len(visit_temp) > 0: #BFS
        start=visit_temp[0]
        for v in ad[start] :
            if color[v] == -1: #未訪問
                visit_temp.append(v)
                color[v] = 0
                
        color[start] = 1
        tree[start] = t
        
        pop_ = visit_temp.popleft()
        visit.append(pop_)
        
tree_={}
for v in set(tree.values()):
    tree_[v]=set()
    
for k in set(tree.keys()):
    tree_[tree[k]].add(k)
    
ans=[]
for n in range(N):
#     print('===')
    n=n+1
    
    tree_len=len(tree_[tree[n]])
    friend_len=len(ad[n])
    
    brock_len=0
    for b in block[n]:
        if tree[n] == tree[b]:
            brock_len += 1
            
#     print(tree_len,friend_len,brock_len)
#     print(tree_len-friend_len-brock_len-1)
    ans.append(tree_len-friend_len-brock_len-1)
            
print(' '.join(map(str,ans)))