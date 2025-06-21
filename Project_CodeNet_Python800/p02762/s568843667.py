n,m,k = map(int,input().split())
ab = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    ab[a-1].append(b-1)
    ab[b-1].append(a-1)
cd = [set([]) for i in range(n)]
for i in range(k):
    c,d = map(int,input().split())
    cd[c-1].add(d-1)
    cd[d-1].add(c-1)
    
ans = [0 for i in range(n)]
data = [0 for i in range(n)] #見たら1
for i in range(n): #自分がi
    if(data[i] != 0): #もう見てたら必要なし
        continue
    data[i] = 1 #iの人を見る
    data2 = ab[i] + [i]
    data2 = set(data2)
    for j in ab[i]:
        data[j] = 1
    new_friends = [ab[i]]
    for fris in new_friends:
        new = [] #次の深さのリスト
        for fri in fris: #この層の友人を１人選ぶ
            for frfr in ab[fri]: #その友人の友人
                if(data[frfr] == 0): #見てなかったら加える
                    data[frfr] = 1 
                    new.append(frfr) #次の深さのリストに足す
                    data2.add(frfr) #グラフに足す
        if(len(new)==0):
            break
        else:
            new_friends.append(new)

    sam = len(data2)
    for j in data2:
        count = sam
        ans[j] = count - len(ab[j]) - len(cd[j] & data2) - 1 #自分と友達を除く


print(*ans)