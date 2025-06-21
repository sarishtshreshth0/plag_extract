# 問題が少しわかりずらい。
n = int(input())
w = list(map(int, input().split()))
a = 10**19
for i in range(1, n-1):
  	# 重りを二つに分け、差異の最小値を判定する。
    a = min(abs(sum(w[:i+1]) - sum(w[i+1:])), a)
print(a)
