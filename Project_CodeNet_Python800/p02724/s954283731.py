X = int(input())
x_500 = X//500
X -= x_500*500
x_5 = X//5
print(1000*x_500 + 5*x_5)