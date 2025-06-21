# 初期入力
import sys
input = sys.stdin.readline
N,M = (int(i) for i in input().split())
X = list(map(int, input().split()))
if N >=M:
    ans =0
else:
    X.sort()
    dif =[-1]*(M-1)
    for i in range(M-1):
        dif[i] =X[i+1] -X[i]
    dif.sort()
    ans =dif[:M-N]
    ans =sum(ans)
print(ans)