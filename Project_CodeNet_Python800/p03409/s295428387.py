N = int(input())

"""考え方
1.青色を第一要素（x）が小さい順にソートする
2.青色の点より左にある赤い点のうち、yが小さく、かつ一番大きい赤い点を選択する
"""

## 1.必要な配列を取得し、x軸でソートしておく
## 1-1.赤色
AB = []
for n in range(N):
  AB.append(list(map(int, input().split())))
  
AB = sorted(AB, key=lambda x: x[1], reverse=True)

## 1-2.青色
CD = []
for n in range(N):
  CD.append(list(map(int, input().split())))
CD = sorted(CD, key=lambda x: x[0], reverse=False)


## 2.青色の点について、左から順に取得していく
used_idx = []
ans = 0
for _ in CD:
  c = _[0]
  d = _[1]
  red_max_y = -1
  ## 左側にある赤色の要素を検索
  for idx, __ in enumerate(AB):
    a = __[0]
    b = __[1]
    if a < c:
      if b < d:
        if idx not in used_idx:
          used_idx.append(idx)
          ans += 1
          break
  
    
print(ans)