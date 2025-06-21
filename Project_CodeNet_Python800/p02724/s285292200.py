X = int(input())
happy = 0

happy += (X // 500) * 1000
X %= 500

happy += (X // 5) * 5

print(happy)