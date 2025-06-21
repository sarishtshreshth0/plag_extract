import numpy as np
n,m = map(int, input().split())
x = np.array([int(i) for i in input().split()])
x = np.sort(x)
d = np.diff(x)
d = np.sort(d)[::-1]
if m < n:
    ans = 0
else:
    '''
    x ---+---+----------+-+----+-
    d    3   10         1 4    -
    このとき、d = 3,1の点を選んでいる
    なぜ？
        d = 10で分割している
    分割したあとは、左から距離を足せばおｋ
    分割の回数はn-1個 -> dの大きいものからn-1個除去し、残りのsumを取る
    '''
    ans = d[n-1:].sum()
print(ans)