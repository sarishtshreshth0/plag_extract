def into_ruiseki(a):
	n = len(a)
	ret = [0 for i in range(n + 1)]
	for i in range(n):
		ret[i + 1] = ret[i] + a[i]
	return ret

n = int(input())
a = list(map(int, input().split()))

b = sorted(into_ruiseki(a))
# print("b =", b)
ans = 0
cnt = 1
for i in range(1, n + 1):
	if b[i] == b[i - 1]:
		cnt += 1
	else:
		ans += cnt * (cnt - 1) // 2
		cnt = 1
ans += cnt * (cnt - 1) // 2
print(ans)