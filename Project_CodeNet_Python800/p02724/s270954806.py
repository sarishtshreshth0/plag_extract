X = int(input())
answer = (X // 500) * 1000
X %= 500
answer += (X // 5) * 5
print(answer)