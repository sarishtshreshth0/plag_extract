from collections import Counter
n = int(input())
d = list(map(int,input().split()))
mod = 998244353

c = Counter(d)
max_d = max(d)#最大の深さを求める
ans = 1
previous_leaf = 1

#頂点1から頂点1の距離が0以外だったらansを0にする
if d[0] != 0:
    ans = 0
#距離0のノードは頂点1のみの1個でなければ不可能
elif c[0] != 1:
    ans = 0
#前の距離のノードa個あったら場所でa通りあり、さらに前の距離のノード1個につき今の距離のノードb個の子がいるので、全部でa**b通り増えてく
else:
    for i in range(1,max_d+1):
        ans *= (previous_leaf**c[i])
        ans %= 998244353

        #前の距離のノード
        previous_leaf = c[i]
print(ans)
