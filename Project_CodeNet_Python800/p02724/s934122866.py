x = int(input())

fivehandred = x // 500
x -= x // 500 * 500
five = x // 5

print(fivehandred*1000+five*5)