# A - Takahashi Calendar
def calc_product(str_day):
	product = 1
	
	for d in str_day:
		if int(d) < 2:
			return 0
		else:
			product *= int(d)
		
	return product


M, D = map(int, input().split())
ans = 0

for m in range(1, M + 1):
	for d in range(22, D + 1):
		if calc_product(str(d)) == m:
			#print(str(m) + '月' + str(d) + '日')
			ans += 1

print(ans)