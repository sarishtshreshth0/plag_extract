X = int(input())

c500 = X // 500
c5 = (X -(c500 * 500)) // 5
answer = (c500 * 1000) + (c5 * 5)

print(answer)