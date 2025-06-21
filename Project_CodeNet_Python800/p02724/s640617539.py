X = int(input())

p = X // 500
q = X % 500
r = q // 5

print(p*1000+r*5)