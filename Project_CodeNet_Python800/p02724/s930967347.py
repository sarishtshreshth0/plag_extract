x = int(input())

cnt_500 = x // 500
cnt_5 = (x % 500) // 5

print(cnt_500 * 1000 + cnt_5 * 5)