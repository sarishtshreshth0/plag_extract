i = input().split()
n1 = max(int(i[0]),int(i[1]))
n2 = min(int(i[0]),int(i[1]))
aa = list(range(n2,n1))
#print(int(i[2]) in aa)
#変数 = 真の場合の代入値 if 条件文 else 偽の場合の代入値

ans = ('Yes' if int(i[2]) in aa else 'No')
print(ans)