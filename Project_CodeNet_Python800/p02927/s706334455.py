m, d = map(int, input().split())

cnt = 0

for m in range(1, m + 1):
	for d in range(1, d + 1):
		d1 = d % 10
		d10 = d // 10
		if d1 >= 2 and d10 >= 2:
			if m == d1 * d10:
				cnt += 1

print(cnt)