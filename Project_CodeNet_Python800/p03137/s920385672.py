import sys

# N: コマ数
# M: 地点数

N,M,*X = map(int, open(0).read().split())

# コマ数が地点数以上の場合、各地点にコマを配置できる
# よって 0 回の移動で目的を達成できる
if N >= M:
    print(0)
    sys.exit()

X.sort()
D = sorted([abs(X[i+1] - X[i]) for i in range(M-1)], reverse=True)
print(X[-1] - X[0] - sum(D[:N-1]))