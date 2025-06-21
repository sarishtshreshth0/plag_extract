n = int(input())
d = {}
mod = 998244353
max_v = 0
lis = list(map(int, input().split()))

# 先頭はかならず0
if lis[0] != 0:
    print(0)
    exit()

for v in lis:
    if v not in d:
        d[v] = 1
    else:
        d[v] += 1
    max_v = max(max_v, v)

# 0はひとつだけ
if 0 not in d or d[0] > 1:
    print(0)
    exit()

ans = 1
# 木を作ることができるならば1~max_vまでの数字がそれぞれ1つ以上存在する
for i in range(1, max_v + 1):
    if i not in d or i - 1 not in d:
        ans *= 0
    else:
        ans *= pow(d[i - 1], d[i], mod)
        ans %= mod
print(ans)