x = int(input())

bigmoney_number = x // 500
bigmoney = x // 500 * 1000
smallmoney = (x - bigmoney_number * 500) // 5 * 5

print(bigmoney + smallmoney)
