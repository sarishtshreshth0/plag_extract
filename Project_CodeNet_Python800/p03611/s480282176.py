def main():
	N = int(input())
	a = list(map(int, input().split()))
	
	a_lst = [0] * (10 ** 5 + 1)
	for num in a:
		a_lst[num] += 1

	ans = 0
	for X in range(10 ** 5 + 1):
		cnt = 0

		if X == 0:
			cnt += a_lst[X]
			cnt += a_lst[X + 1]
		elif X == 10 ** 5:
			cnt += a_lst[X - 1]
			cnt += a_lst[X]
		else:
			cnt += a_lst[X - 1]
			cnt += a_lst[X]
			cnt += a_lst[X + 1]

		if cnt > ans:
			ans = cnt

	print(ans)



 
if __name__ == "__main__":
  	main()