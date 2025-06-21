X = int(input())

total = 0
happiness_500 = X // 500 *1000 
total += happiness_500
y = X % 500
happiness_5 = y //5 *5
total += happiness_5
print(total)