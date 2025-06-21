N = int(input())
D = list(map(int, input().split()))
mod = 998244353
counter = [0] * N
for d in D:
    counter[d] += 1

if counter[0] != 1:
    print(0)
    exit()

ans = 1
for d in D[1:]:
    ans = ans * counter[d-1] % mod
print(ans)