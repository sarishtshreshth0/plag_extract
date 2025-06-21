def nikkei19q_b():
    _ = int(input())
    D = list(map(int, input().split()))
    div = 998244353

    dmax = max(D)
    cntr = [0] * (dmax + 1)
    for d in D: cntr[d] += 1  # カウンター

    if D[0] != 0: return 0  # 最初に入力される頂点1は距離0マスト
    if cntr[0] != 1: return 0  # 距離0が無い、または2つ以上、はおかしい

    ans = 1
    for i in range(1, dmax+1):
        if cntr[i] == 0: return 0  # カウント0だとつながらないのでNG
        ans = ans * (cntr[i-1] ** cntr[i]) % div
    return ans

print(nikkei19q_b())