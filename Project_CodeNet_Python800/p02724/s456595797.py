money = int(input())

count_div_500, left_after_500 = divmod(money, 500)
count_div_5, left_after_5 = divmod(left_after_500, 5)

print(count_div_500 * 1000 + count_div_5 * 5)
