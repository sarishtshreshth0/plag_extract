x = int(input())

count_500 , mod = divmod(x, 500)
count_5 = mod // 5
print(count_500 * 1000 + count_5 * 5)