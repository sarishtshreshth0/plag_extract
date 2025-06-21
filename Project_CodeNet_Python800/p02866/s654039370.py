MOD = 998244353

n = int(input())
d_lst = list(map(int, input().split()))
if d_lst[0] != 0:
    print(0)
    exit()

max_d = max(d_lst)
lst = [0 for _ in range(max_d + 1)]
for d in d_lst:
    lst[d] += 1
if lst[0] != 1:
    print(0)
    exit()
ans = 1
for i in range(max_d):
    ans *= pow(lst[i], lst[i + 1], MOD)
    ans %= MOD
print(ans)