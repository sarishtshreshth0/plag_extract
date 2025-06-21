MOD = 998244353

N = int(input())
D = list(map(int,input().split()))

cnt = [0] * N
for i in range(N):
	cnt[D[i]] += 1

if D[0] != 0 or cnt[0] > 1:
	print(0)
	exit()

ans = 1
for i in range(1, max(D) + 1):
	ans = (ans * pow(cnt[i - 1], cnt[i], MOD)) % MOD
print(ans)