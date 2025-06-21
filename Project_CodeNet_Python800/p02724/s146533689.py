X = int(input())
c1 = X//500
X = X - c1*500
c2 = X//5
print(c1*1000 + c2*5)