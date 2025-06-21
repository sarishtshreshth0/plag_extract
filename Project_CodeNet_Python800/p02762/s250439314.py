from collections import defaultdict
from collections import deque

n,m,k = map(int,input().split())

f_set = {tuple(map(int,input().split())) for _ in range(m)}

b_set = {tuple(map(int,input().split())) for _ in range(k)}


friends_counts = {key:[] for key in range(1,n+1)}
blocks_counts = {key:[] for key in range(1,n+1)}

for f in f_set:
    friends_counts[f[0]].append(f[1])
    friends_counts[f[1]].append(f[0])

for b in b_set:
    blocks_counts[b[0]].append(b[1])
    blocks_counts[b[1]].append(b[0])



friends_groups_list = [set() for _ in range(n+1)]

#dfs
que = deque()
groups_count = 0
checked_dict = {key:0 for key in range(1,n+1)}
#que.appendleft(1)

for i in range(1,n+1):
    if checked_dict[i] == 1:
        continue
    que.appendleft(i)
    checked_dict[i] = 1

    while que:
        x = que.popleft()
        friends_groups_list[groups_count].add(x)
        for i in range(len(friends_counts[x])):
            if checked_dict[friends_counts[x][i]] == 0:
                que.appendleft(friends_counts[x][i])
            checked_dict[friends_counts[x][i]] = 1

    groups_count += 1



result_list=[0]*n

#print(blocks_counts)
#print(friends_groups_list)

for i in range(len(friends_groups_list)):
    mini_set = friends_groups_list[i]
    for ms in mini_set:
        result_list[ms-1] = len(mini_set) - 1 - len(friends_counts[ms])
        
        block_counter_in_minilist = 0

        for k in blocks_counts[ms]:
            if k in mini_set:
                block_counter_in_minilist += 1
        
        result_list[ms-1] -= block_counter_in_minilist
 
print(" ".join(map(str,result_list)))



#cの配列の解釈が違ったらしい。。。
#f_set = {tuple(map(int,input().split())) for _ in range(m)}
#
#b_set = {tuple(map(int,input().split())) for _ in range(k)}
#
#c_list = [0] * (n-1)
#
#result_dict = {key:0 for key in range(1,n+1)}
#
#for f in f_set:
#    if abs(f[0]-f[1]) == 1:
#        c_list[min(f[0],f[1]) - 1] = 1
#    #ここでelseで飛び石での友達のsetを作ってもよいが、そもそもsetなのでinでの探索にそんなに時間かからないし、いったんこのままやってみる。
#
#for start in range(0,n-2):
#    if c_list[start] == 0:
#        #c[start]が1になるまで飛ばす
#        continue
#
#    for end in range(start+1,n-1):
#        if c_list[end] == 0:
#            #友人同士ではないペアまできたらstartをインクリメント
#            break
#        
#        #もし「友人候補」の候補者が、「友人関係でない」かつ「ブロック関係でない」ことをチェックしている。
#        if not (start+1,end+2) in f_set and not (end+2,start+1) in f_set and not (start+1,end+2) in b_set and not (end+2,start+1) in b_set:
#            result_dict[start+1] += 1
#            result_dict[end+2] += 1
#
#for i in range(1,n+1):
#    print(result_dict[i])
#
#print(c_list)

