def agc023_a():
  n = int(input())
  A = list(map(int, input().split()))
  # 累積計算していき、通った地点と回数をカウント
  acc = 0
  transit = dict({0:1})
  for a in A:
    acc += a
    if transit.get(acc) == None:
      transit[acc] = 1
    else:
      transit[acc] += 1
  # 複数回通った地点どうしの区間の和は0
  # v個から2個選ぶ
  ans = 0
  for k, v in transit.items():
    if v >= 2:
      ans += v * (v-1) // 2
  print(ans)

agc023_a()