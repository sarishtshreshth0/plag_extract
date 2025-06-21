def calc_digits(num):
	ans = 1

	while True:
		if num // 10 == 0:
			break

		num //= 10
		ans += 1

	return ans


def main():
	N = int(input())

	n = int(N ** 0.5)
	ans = 10 ** 10

	for A in range(1, n + 1):
		if N % A == 0:
			B = int(N / A)
		else:
			continue

		A_digits = calc_digits(A)
		B_digits = calc_digits(B)

		max_digits = max(A_digits, B_digits)

		if max_digits < ans:
			ans = max_digits

	print(ans)



  
if __name__ == "__main__":
  	main()