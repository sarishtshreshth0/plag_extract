x = int(input())
count_500 = 0
count_5 = 0
count_500 = x // 500
x -= 500 * count_500
count_5 = x // 5
x -= 5 * count_5
print(1000 * count_500 + 5 * count_5)