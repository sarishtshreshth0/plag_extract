X = int(input())

happy1 = X // 500
X -= 500 * happy1
happy2 = X // 5
print(happy1*1000 + happy2*5)