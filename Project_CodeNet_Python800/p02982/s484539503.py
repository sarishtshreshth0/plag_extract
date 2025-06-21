n, d = map(int, input().split())
num_list = []
cnt = 0

#2次元リスト作成
for i in range(n):
    num_list.append(list(map(int, input().split())))

#j<kのもとでループ
for j in range(n):
    for k in range(j + 1, n):
        c = 0
        for l in range(d):
            c += (num_list[j][l] - num_list[k][l]) ** 2
    
        if (int(c**0.5))**2 == c :
            cnt += 1
        
print(cnt)