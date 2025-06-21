x = int(input())

cnt_500 = 0
cnt_5 = 0
while x > 4:
    if x >= 500:
        x -= 500
        cnt_500 += 1
    else:
        x -= 5
        cnt_5 += 1

print(1000*cnt_500+5*cnt_5)
