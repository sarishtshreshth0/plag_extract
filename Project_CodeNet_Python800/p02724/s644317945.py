x = int(input())

result = 1000 * (x // 500)
x -= 500 * (x // 500)
result += 5 * (x // 5)
print(result)