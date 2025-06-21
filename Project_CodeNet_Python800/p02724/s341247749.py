x = int(input())
answer = 0
answer = (x//500)*1000
x = x%500
answer += (x//5)*5
print(answer)