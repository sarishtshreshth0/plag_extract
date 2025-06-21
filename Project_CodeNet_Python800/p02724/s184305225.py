X = int(input())
Y = X % 500
answer = (X // 500 * 1000 + Y // 5 * 5)
print(answer)