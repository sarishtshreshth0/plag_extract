import collections
n = int(input())
d = list(map(int, input().split()))
mod = 998244353
f = collections.Counter(d)
# print(f)
if d[0] != 0 or f[0] != 1:  # 0は一個だけ
    print(0)
    exit()
ans = 1
box = 1  # 値自体の個数を保存
maxd = max(d)

for i in range(maxd+1):
    ans = ans*box**f[i]
    ans %= mod
    box = f[i]
print(ans)
