x = int(input())

c_500 = 0
c_5 = 0
while True:
    temp = x - 500
    if temp < 0:
        break
    else:
        c_500 += 1
        x = temp

while True:
    temp = x - 5
    if temp < 0:
        break
    else:
        c_5 += 1
        x = temp

print(c_500 * 2 * 500 + c_5 * 5)
