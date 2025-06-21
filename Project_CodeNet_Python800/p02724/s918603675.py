X = int(input())
happy = 0
big_fun = 0
small_fun = 0
big_fun = X // 500
X = X % 500
small_fun = X // 5

happy = big_fun * 1000 + small_fun * 5

print(happy)