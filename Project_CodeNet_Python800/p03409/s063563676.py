n = int(input())
r = [list(map(int, input().split())) for _ in range(n)]
r.sort(key=lambda x: x[1], reverse=True)  # redはyを昇順でソート
b = [list(map(int, input().split())) for _ in range(n)]
b.sort()  # blueはxが降順にソート
cnt = 0  # cntの初期の設定
for i in range(n):  # blueのxが小さい方から全探索
    for j in range(len(r)):
        if r[j][0] < b[i][0] and r[j][1] < b[i][1]:
            cnt += 1
            r.pop(j)
            break
print(cnt)
