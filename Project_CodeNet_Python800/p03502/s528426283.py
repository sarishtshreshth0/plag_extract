def calc_sum_of_digits(num):
	ans = 0

	while True:
		if num // 10 == 0:
			ans += num
			break

		ans += num % 10
		num //= 10

	return ans



def main():
	N = int(input())

	sum_of_digits = calc_sum_of_digits(N)

	if N % sum_of_digits == 0:
		print("Yes")
	else:
		print("No")


  
if __name__ == "__main__":
  	main()